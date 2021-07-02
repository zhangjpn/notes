# cosmic python


## 摘要

one aggregate = one repository
The rule that repositories should only return aggregates is the main place where we enforce the convention that aggregates are the only way into our domain model. Be wary of breaking it!

Repository 应该只返回aggregate，也就是说，aggregate是接触领域模型的唯一方式


```py


class Domain(object):
    """业务领域模型"""
    name = 'name'


class Repository(object):
    """隔离数据库与领域模型的一个层"""
    # 将聚合作为一个完整的领域模型对外提供
    aggregate = Aggregate()

    def get():
        return self.aggregate


class Aggregate(object):
    """聚合，对外的抽象领域模型组合"""
    # 将边界内的领域模型聚合在一起作为一个整体对外
    domain = Domain()
    domain2 = Domain()
    

class UnitOfWork(object):
    """工作单元，封装事务"""
    product = Aggregate()

    pass


class Service(object):
    """接口层"""
    def do_post(self):
        uow = UnitOfWork()
        with uow:
            product = uow.products.get()
            product.change()

            uow.commit()
    

```


Part 2: Event-Driven Architecture
事件驱动架构

The key in making great and growable systems is much more to design how its modules communicate rather than what their internal properties and behaviors should be.
构建更大更可成长系统的关键是设计模块间如何通信而不是他们各自内部的属性和行为如何。


常见的将单体划分为微服务的思路是将系统划分成若干名词的组合，而系统之间的通信是通过命令流来实现，也就是一个服务命令另一个服务执行某个动作。

这种划分相当于每个数据表对应一个服务，这能应付简单的应用，但对复杂的系统很快会乱成一团。

When two things have to be changed together, we say that they are coupled. 

解耦：用动词去思考拆分

将触发方式分成两类：事件和命令，http请求是命令

- Domain Events pattern
- Message Bus pattern
- Primitive Obsession（基本型别偏执）
- 
https://www.kancloud.cn/sstd521/refactor/194219

events挂在model中，通过repository监控和获取

* 服务层依赖于抽象

NOTE:
- Repository 隔离了底层数据与模型
- unit of work 抽象了事务
- event bus 解耦，实现职责分离（单一职责原则）
- cqrs + event sourcing
- 

项目结构
```txt
一个微服务可以包含多个界限上下文，也可以只包含单个界限上下文，微服务是物理的边界，而不是概念边界。
微服务底层的aggrgate才是界限上下文，在此基础上构建的需要实现多个aggregate一致性的事务就是分布式事务。
/project/
    services/
        aggregate1/ 在这个底层内定义属于这个界限上下文的所有内容，然后在上层将其调用
            event1
            event2

        aggregate2/
            event3
            event4



```


### 13: Dependency Injection (and Bootstrapping)
依赖注入的目的是为了解耦上层对底层的依赖，并且易于测试
bootstrapping的目的是为了解决每次调用都要单独实例化所需依赖的问题，创建集中式的bootstrap脚本来实现对通用依赖的实例化。

#### DIP/IOC/DI
DIP, Dependence Inversion Principle，依赖倒置原则，即面向接口编程，上层功能不关心底层依赖的实现
IOC, Inversion of Control 控制反转，关注的是上层不关注底层的创建，而应该是调用者先创建好（初始化），再传入调用函数中
DI , Dependency Injection 依赖注入，是实现控制反转的手段，将实例化好的依赖传入到调用函数中





