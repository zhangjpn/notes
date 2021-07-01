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

import werkzeug
from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app)

@app.errorhandler(500)
def handle_500(e):
    return 
    
@app.errorhandler(Exception)
def handle_unknown_error(e):
    pass

@api.errorhandler(werkzeug.exceptions.InternalServerError)
def handle_internal_error(e):
    pass
@api.errorhandler(werkzeug.exceptions.NotFound)
def handle_page_not_found_error(e):
    pass
```
