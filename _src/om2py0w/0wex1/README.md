# 交互101

本周整体任务概述:

* 完成一个极简交互式日记系统,需求如下:
    * 一次接收输入一行日记
    * 保存为本地文件
    * 再次运行系统时,能打印出过往的所有日记
* 时限: 0wd4~1wd3
* 发布: 发布到各自仓库的 `_src/om2py0w/0wex1/` 目录中
* 指标:
    * 包含软件使用说明书: `README.md`
    * 能令其它学员根据说明书,运行系统,完成所有功能
    
## 功能使用说明
1. 接受一个参数，作为日志文件名称
2. 脚本运行后，首先根据给出的日志文件名称，读取已有的日志信息并打印
    * 如果给出的日志名称不存在，则打印相关提示信息，进入下一阶段
3. 开始接受用户输入，以`> `作为提示符，每次接受用户一行输入
4. 用户键入`exit`并敲回车后，退出脚本
5. 用户键入`history`命令后，打印目前为止的日记内容
6. 运行方法`python main.py <log_file_name>`
7. 用户键入`python main.py`的时候，使用`history.log`作为日记文件，参数个数超过一个的时候，打印`usage`信息

## 学习记录
* git add [-f]
* git commit -m "message"
* git remote add \<name\> \<url\> 
    * 注意url的格式，如果是https开头的，则每次push的时候需要输入用户名密码
    * 如果url是ssh格式的，则可以通过互信来提交
* git remote -v
* git push \<remote host\> \<local branch\>:\<remote branch\>