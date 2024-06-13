# API docs specification

## 介绍

互联网应用通过接口提供服务，这种接口可以通过统一的规约(specification)进行描述，流行的规约包括openAPI和raml。

## openAPI

OpenAPI规约(OAS)又可分为2.x和3.x版本，2.x版本被称为swagger2.0，因为openapi是从swagger演化而来的。
目前常用三个版本的openapi规约，3.x版本与2.x版本不完全兼容。

### 工具

- [swagger-ui](https://swagger.io/tools/swagger-ui/): 负责呈现规约，可以直接作为客户端发送请求，本质上是一个web前端网页，可以读取规约文件并渲染成可交互发情求的页面
- [editor](https://swagger.io/tools/swagger-editor/)：辅助规约文件编辑
- [codegen](https://swagger.io/tools/swagger-codegen/)：通过规约文件生成各种语言的stub和client

### 写法

- [swagger2](https://swagger.io/docs/specification/2-0/basic-structure/)
- [openapi3.0](https://swagger.io/docs/specification/about/)
- [openapi3.1](https://swagger.io/specification/)

OpenAPI可以使用yaml或json格式描述，OAS3.0的demo：

```yaml
openapi: 3.0.3  # swagger: 2.0 / openapi: 3.1.0

info:
    - description: A demo service
    - version: 1.0.1
    - title: DEMO API

servers:
  - url: https://abc-dev.com
    description: dev env
  - url: https://abc-uat.com
    description: uat env
  - url: /  # set default to current host

components:
  responses:
    UnauthorizedError:
      description: unauthorized
  schemas:
    UserItem:
      type: object
      properties:
        id:
          type: integer
          required: true
          description: ID for user
        name:
          type: string
      required:
        - id
        - name
  parameters:
    offsetParam:  # <-- Arbitrary name for the definition that will be used to refer to it.
                  # Not necessarily the same as the parameter name.
      in: query
      name: offset
      required: false
      schema:
        type: integer
        minimum: 0
      description: The number of items to skip before starting to collect the result set.
    limitParam:
      in: query
      name: limit
      required: false
      schema:
        type: integer
        minimum: 1
        maximum: 50
        default: 20
      description: The numbers of items to return.
paths:
  /index:
    get:
      summary: short description
      tags:
        - index
      description: long description
      parameters:
        - $ref: '#/components/parameters/offsetParam'
        - $ref: '#/components/parameters/limitParam'
      requestBody:
      responses:
        '200':
          description: success
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
        '400':
          description: bad request


```

### 集成

- flask：可以使用第三方库：flasgger、flask-swagger-ui，一些restful框架自带
- fastapi：通过注解自动生成
