# logging

## 调用逻辑

![日志调用流](../../static/imgs/logging_flow.png)
出自[官网](https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial)

为什么有些第三方库的调试日志写死用自定义的logger，而有些则允许传入指定的logger？

比如，flask用的是自定义的logger，而apscheduler则支持logger

我个人的思考是，作为一个服务框架，应当支持传入自定义的logger，因为使用时作为一个服务持续运行，需要持续监控其中的工作环节，而其他的工具类库，一般只有工具开发过程中的测试、调试阶段会用到日志，应用在使用的时候很少需要内部的日志细节。

像gunicorn这样的库没有提供完善的日志库的注入方法，只能根据它的名字拿到它内部的logger。

## 零碎

1. 使用第三方库中使用的__name__指向顶层包名，与应用名称无关。如requests中使用的logging.getLogger(__name__)，其logger名称是request。
2. 默认情况下，logger有个propagate属性，默认为true
3. root logger默认level为WARNING，其它logger默认level为NOTSET，也就是说，自己创建的logger，如果不设置level，则所有级别的都会打印
4. logger继承关系使用"."表示，例如"parent.child"，无论在什么文件，只要名称相同，拿的就是相同的logger
