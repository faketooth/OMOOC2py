# -*- coding: utf-8 -*-

from bottle import route, run, debug, template, request


@route('/')
def index():
	return template('index.tpl')
	
@route('/browse')
@route('/history')
@route('/reading')
def browse():
	diary = open('diary.txt', 'r')
	lines = diary.readlines()
	diary.close()
	return template('reading.tpl', content=lines)
	
@route('/writing')
@route('/new')
@route('/new_diary')
def new_diary():
	if request.GET.get('save','').strip():
		newline=request.GET.get('newline', '').strip()
		if newline == '':
			return template('new_diary.tpl')
		diary = open('diary.txt', 'a')
		diary.write(newline + '\n')
		diary.close()
	return template('new_diary.tpl')
	
	
debug(True)
run(reloader=True)