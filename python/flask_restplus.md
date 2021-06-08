# flask-restplus插件使用

## 概述



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

