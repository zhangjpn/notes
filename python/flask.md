# Flask笔记

## 常用命令

```shell
# 创建虚拟环境
$ python -m venv venv
# 或
$ virtualenv -p /path/to/python venv
# 激活虚拟环境
$ source venv/bin/activate
# 安装依赖
$ pip install -r requirements.txt
# 输出依赖
$ pip freeze > requirements.txt

# flask 环境变量
$ export FLASK_APP=microblog.py
# 调试模式
$ export FLASK_DEBUG=1
# 内置服务，用于调试
$ flask run


# 数据库迁移
# flask-migrate 扩展支持
# 生成一份迁移脚本
$ flask db migrate -m "迁移说明"
# 执行数据库变更(真实发生的数据库变更)
$ flask db upgrade
# 

```

### 多app合并

```py3

from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask
# from threading import get_ident
from flask import request
from greenlet import getcurrent as get_ident

frontend = Flask('frontend')
backend = Flask('backend')


@frontend.route('/home')
def home():
    i = get_ident()
    print('frontend get_ident: %s' % i)
    return 'frontend home'


@frontend.route('/home1')
def home1():
    i = get_ident()
    print('frontend1 get_ident: %s' % i)
    return 'frontend home'


@backend.route('/home')
def home():
    i = get_ident()
    print('backend get_ident: %s' % i)
    return 'backend home'


app = DispatcherMiddleware(frontend, {
    '/frontend': frontend,
    '/backend': backend
})

if __name__ == "__main__":
    run_simple('127.0.0.1', 5000, app)
```

## Flask 技术栈

- restful框架:
  - flask-restx
  - connexion
  - flask-restful
- 鉴权
  - flask-jwt-extended
  - flask-security
- 集合
  - flask-appbuilder: 差不多实现了Django的效果，但是因为集合的插件由不同开发者维护，所以只能用比较旧的版本，既然用集合，为什么不直接用Django？
- 数据校验
  - marchmallow
  - pydantic
  - flask-pydantic: 对pydantic的简单封装，需要尽早引入，使得flask跟pydantic形成强耦合，不是特别好用
  - attrs
- ORM
  - sqlalchemy
