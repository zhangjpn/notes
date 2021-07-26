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

## 笔记

### Part1: Building an Architecture to Support Domain Modeling

#### chapter 06

工作单元（unit of work）的引入是为了提供一个一致性的会话，在这个地方提供事务功能，这事务既可以是单个数据库事务，也可以实现分布式事务。这是将多个服务组合起来的最小单元，也是将多个repository通过共同的session组合起来的地方。
repository则是提供提供聚合根的仓库。在书中，这个聚合根就是后面章节提到的Product。

#### chapter 07

The Aggregate pattern is a design pattern from the DDD community that helps us to resolve this tension. An aggregate is just a domain object that contains other domain objects and lets us treat the whole collection as a single unit.

一个聚合加载的时候会将其内部所包含的所有东西都加载进来，构成一个对象，这会造成性能问题，怎么解决？
    - 相对于多次即时查询，一次加载所需的所有东西在很多甚至大多数场景下性能更好
    - lazy-loading

aggregate的选择应该尽可能小，出于性能原因，也应该足够大，以囊括所有相关联的事物。

aggregate不必对应某个实际存在的事物，而应该将其作为一堆基于某个目的而存在的事物的集合，一个聚合就是一个一致性边界。

one aggregate = one repository

通过版本号实现乐观并发控制：这实际上就是基于版本号的乐观锁，乐观锁需要处理冲突之后的重试。
版本号的控制控制权问题：由于它本质上属于基础设施的东西，所以理论上应该放到数据库读写的repository中，但是放到这里可能会出现不必要的数据更新，所以最直接的方式是放在domain中。

- boundary context
- aggregate

### Part 2: Event-Driven Architecture

事件驱动架构

The key in making great and growable systems is much more to design how its modules communicate rather than what their internal properties and behaviors should be.
构建更大更可成长系统的关键是设计模块间如何通信而不是他们各自内部的属性和行为如何。

常见的将单体划分为微服务的思路是将系统划分成若干名词的组合，而系统之间的通信是通过命令流来实现，也就是一个服务命令另一个服务执行某个动作。

这种划分相当于每个数据表对应一个服务，这能应付简单的应用，但对复杂的系统很快会乱成一团。

When two things have to be changed together, we say that they are coupled.

解耦：用动词去思考拆分

将触发方式分成两类：事件和命令，http请求是命令

- Domain Events pattern：一致性边界是aggregate/repository，event应该放到aggregate之外进行调度？
  - events挂在model中，通过repository监控和获取

- Message Bus pattern：
- CQRS：提升性能

- Primitive Obsession（[基本型别偏执](https://www.kancloud.cn/sstd521/refactor/194219)）

服务层依赖于抽象

NOTE:

- Repository 隔离了底层数据与模型
- unit of work 抽象了事务
- event bus 解耦，实现职责分离（单一职责原则）
- cqrs + event sourcing

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

### 09：Going down on the message bus

将所有请求看作是事件，web服务的工作就是不断处理事件。由于处理事件是不会返回处理结果的，所以需要配合cqrs，将查询和命令进行分离，把请求当做命令。

### 11：Event-Driven Architecture： Using Events to Integrate Microservices

### 13: Dependency Injection (and Bootstrapping)

依赖注入的目的是为了解耦上层对底层的依赖，并且易于测试
bootstrapping的目的是为了解决每次调用都要单独实例化所需依赖的问题，创建集中式的bootstrap脚本来实现对通用依赖的实例化。

#### DIP/IOC/DI

DIP, Dependence Inversion Principle，依赖倒置原则，即面向接口编程，上层功能不关心底层依赖的实现
IOC, Inversion of Control 控制反转，关注的是上层不关注底层的创建，而应该是调用者先创建好（初始化），再传入调用函数中
DI , Dependency Injection 依赖注入，是实现控制反转的手段，将实例化好的依赖传入到调用函数中

## 其他

### DDD blue book

Part 1：如何构建合适的aggregate

一个aggregate是一个最小的事务变动单位（可以粗略地理解），一致性边界要求其中的事务达到强一致性。
An aggregate is an minimal invariant.
An invariant is a business rule that must always be consistent.

Part 2：如何处理多aggregate的最终一致性

一个aggregate通过id引用另一个aggregate。

通过Domain event将事件通过message bus（消息总线）传递到其他的aggregate中进行消费。

对于消费事件时发生失败的情况可以进行重试，重试失败可以使用补偿或人工介入的方式解决。

Part 3：

估算加载一个aggregate需要多少成本（加载多少对象，有多高频的场景会需要用到）
