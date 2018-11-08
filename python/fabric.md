fabric/fabric3
fabric还不支持python3.x，但是已经有人fork了一个分支成为fabric3能够兼容python2和python3.4+。
https://github.com/mathiasertl/fabric 
安装fabric3
pip uninstall fabric
pip install fabric3

使用

fabfile.py里面纯粹就是编写一个python文件，在里面定义一些函数，使用fab命令的时候可以直接找到该文件下的函数并执行。
在操作函数中可以通过fabric提供的api对远程或本地主机进行操作，就跟脚本操作一样。

https://ruiaylin.github.io/2014/11/24/fabric/

fabric主要接口方法fabric.operations.*/fabric.api.*
sudo()
run()
runmkdir()
local()
get()
put()
promopt()
reboot()
上下文管理器fabric.context_managers.*
cd()
lcd()
path()
settings()
prefix()

fabric环境变量env


-------------------------------
# fabfile.py
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['my_server']  # fabric提供的环境变量，除了提供远程主机之外，还提供密码等参数，主机可以写成标准形式username@host:port

def test():
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def commit():
    local("git add -p && git commit")

def push():
    local("git push")

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    code_dir = '/srv/django/myproject'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
---------------------------------