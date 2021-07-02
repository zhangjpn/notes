# flask-restplus插件使用

## 概述

`flask-restplus`作者失联，维护人员已经fork出`flask-restx`，后者完全兼容前者，建议用后者进行开发。

## 使用

### api文档功能

```py
from flask_restplus import Api, Resource, fields

api = Api()

class ResourceA(Resource):
    @api.header()
    @api.params()
    @api.response()
    @api.doc()
    def get(self, user_id):
        pass

# 上述几个最终调用的都是api.doc()方法，只是从不同程度进行了封装，简化了参数和场景


def doc(params=params, body=body, responses=response):
    pass

# 接收以下参数：

params= {
    'field_name': {
        'in': 'header', # header/query/body/...
        'type': str,
        'description': 'desc',
        'required': True,
    }
}
body = mod  # 接收一个model 源于 mod = api.model('model_name', model_definition)

responses = {
    200: ('描述', mod),
    204: ('描述2', mod2),
}

```

### 错误处理

- flask-restplus的errorhandler会拦截掉flask的所有errorhandler，所以用这个包定义的接口的报错需要使用@api.errorhandler(Error)进行处理。
- 如果没有定义errorhandler，则会调用其内部默认的处理函数，但是不会抛出给flask。
- flask-restplus的errorhandler是针对特定的错误类，而不包含其子类。例如处理Exception的handler只能处理Exception，而不会处理Exception派生的错误

最佳实践：

```py
"""测试flask_restplus日志打印问题"""

# flask-restplus的错误处理函数会拦截flask原来的函数

import logging

import werkzeug
from werkzeug.exceptions import HTTPException

# from flask_restx import Api, Resource
from flask_restplus import Api, Resource
from flask import Flask, abort, jsonify


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
api = Api(app)


class MyError(Exception):
    pass


class InvalidParameter(MyError):
    pass


@app.route('/index')
def index():
    abort(500)

class User(Resource):

    def get(self):
        # 无论什么Error，都会抛给api

        # 有注册时，针对性处理
        raise InvalidParameter('my error here')

        # 没注册，但是HttpException, 还是被fr捕获处理
        # raise werkzeug.exceptions.Unauthorized('11111')

        # 没注册特定处理函数，但是注册了默认处理函数
        # raise AttributeError(11)

        # 也没注册默认的，就当是500内部错误了，但也是fr处理掉了
        # 要将错误抛出给app，就要在上面处理时报错，此时会跳过处理，用app的做处理

        return 'ok'


api.add_resource(User, '/user')


@api.errorhandler
def handle_all_error(e):
    raise e


@api.errorhandler(MyError)
def handle_my_error(e):
    logger.error('handle my error: %s', e)
    return {'error': str(e), 'code': 1}, 400


# 最佳实践
@app.errorhandler(Exception)
def HandleAll(e):
    return


# 其他属于flask但不路由到api上处理的接口错误统一由最外层处理
@app.errorhandler(404)
def handle_not_found_error(e):
    return


@app.errorhandler(400)
def bad_request(e):
    return


# @api.errorhandler(InvalidParameter)
# def handle_invalid_parameter(e):
#     """处理业务上的错误"""
#
#     return {'status': -2}, 400


@api.errorhandler(MyError)
def handle_my_error(e):
    """根据捕捉父类错误"""
    # 需要注意的是不同版本对异常类继承的捕获方法不一样
    # 低版本（如：0.9.2）使用errors[e.__class__]的方式匹配，只能捕捉指定的类
    # 高版本则使用了isinstance()来判别，所以可以根据父类来捕获子类

    return {'status': -1}, 400


@api.errorhandler(HTTPException)
def handle_http_error(e):
    """处理http错误"""
    return


@api.errorhandler
def handle_known_error(e):
    """处理未知错误"""
    # 抛出给flask处理
    # raise e
    # 或自己处理
    return {}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, use_reloader=True, debug=True)

```
