# -*- coding: utf-8 -*-
import hashlib
import time
import xml.etree.ElementTree as ET
import urllib2
import json
import mysql.connector
from bottle import route, run, debug, template, request

cnx = mysql.connector.connect(user='diary',password='diary123',host='10.142.135.12',database='diary',buffered = False)

@route('/test', method='GET')
@route('/',method='GET')
def checkSignature():
    token = "YmQOb1C4nH7VbX4"
    signature = request.GET.get('signature', None) 
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    tmpList = [token, timestamp, nonce]
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    hashstr = hashlib.sha1(tmpstr).hexdigest()
    if hashstr == signature:
        print hashstr
        print signature
        return echostr
    else:
        print 'attack!'
        return None

def parse_msg():
    """
    这里是用来解析微信Server Post过来的XML数据的，取出各字段对应的值，以备后面的代码调用，也可用lxml等模块。
    """
    recvmsg = request.body.read()
    root = ET.fromstring(recvmsg)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg

def query_movie_info():
    movie = """
    """
    return movie


def query_movie_details():
    description = """
    """
    return description

@route("/test", method="POST")
@route("/", method='POST')
def response_msg():
    msg = parse_msg()
    if(msg['Content'].startswith('#')):
        content = msg['Content'].encode('utf8')
        msg['Content']="""日记已经记录"""
        sql = """insert into diary(fromuser, msgid,touser, content,msgtype,createtime) values (%r, %r, %r, '%s', %r, %r)""" % (msg['FromUserName'],int(msg['MsgId']),msg['ToUserName'], content[1:],msg['MsgType'], int(msg['CreateTime']))
        cnx.cursor().execute(sql)
        cnx.commit()
    elif (msg['Content'] == 'history'):
        content=u"""至今为止的日志:"""
        sql = """select content from diary.diary t where t.fromuser = %r order by t.createtime asc""" % (msg['FromUserName'])
        cursor = cnx.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        for record in results:
            content = content + "\n" + record[0]
        msg['Content']=content
        
    else:
        msg['Content']="""输入h获取帮助文档
所有日记内容以#开头
查看过往内容，输入history"""
    #纯文本格式
    textTpl = """<xml>
             <ToUserName><![CDATA[%s]]></ToUserName>
             <FromUserName><![CDATA[%s]]></FromUserName>
             <CreateTime>%s</CreateTime>
             <MsgType><![CDATA[%s]]></MsgType>
             <Content><![CDATA[%s]]></Content>
             <FuncFlag>0</FuncFlag>
             </xml>"""
    #图文格式
    pictextTpl = """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>1</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[%s]]></Title>
                <Description><![CDATA[%s]]></Description>
                <PicUrl><![CDATA[%s]]></PicUrl>
                <Url><![CDATA[%s]]></Url>
                </item>
                </Articles>
                <FuncFlag>1</FuncFlag>
                </xml> """
    if msg["Content"] == "Hello2BizUser":
        echostr = textTpl % (
            msg['FromUserName'], msg['ToUserName'], str(int(time.time())), msg['MsgType'],
            u"welcome")
        return echostr
    else:
        echostr = textTpl % (msg['FromUserName'],msg['ToUserName'], str(int(time.time())), msg['MsgType'],		msg['Content'] )
        return echostr


debug(False)
run(host='121.42.216.150',port=80,reloader=True)
