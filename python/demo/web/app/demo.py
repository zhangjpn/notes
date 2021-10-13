import inspect
import logging

logger = logging.getLogger(__name__)


class Message(object):
    pass


class Command(Message):
    pass


class Event(Message):
    pass


class AbstractUnitOfWork(object):

    def __init__(self):
        self.new_events = []

    def collect_new_events(self):
        v = self.new_events
        self.new_events = []
        return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _commit(self):
        pass

    def _rollback(self):
        pass


def DEFAULT_SESSION_FACTORY():
    return 'session'


class SqlalchemyRepo(object):

    def __init__(self, session):
        self.session = session

    def get(self, product_id):
        return 'product'


class SqlalchemyUnitOfWork(AbstractUnitOfWork):

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        super().__init__()  # todo: super()用法
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.products = SqlalchemyRepo(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._rollback()


class MessageBus(object):

    def __init__(self, command_handlers, event_handlers, unit_of_work):
        self.command_handlers = command_handlers
        self.event_handlers = event_handlers
        self.msg_queue = []
        self.unit_of_work = unit_of_work

    def handle(self, msg: Message):
        self.msg_queue = [msg]
        while self.msg_queue:
            m = self.msg_queue.pop(0)
            if isinstance(m, Command):
                self.handle_command(m)
            if isinstance(m, Event):
                self.handle_event(m)
            raise TypeError

    def handle_command(self, command: Command):
        handlers = self.command_handlers.get(type(command))
        for handler in handlers:
            try:
                handler(command)
                self.msg_queue.extend(self.unit_of_work.collect_new_events())
            except Exception as e:
                print(e)

    def handle_event(self, event: Event):
        handlers = self.event_handlers.get(type(event))
        for handler in handlers:
            try:
                handler(event)
                self.msg_queue.extend(self.unit_of_work.collect_new_events())
            except Exception as e:
                print(e)


class UserCreated(Event):
    pass


class NotificationSent(Event):
    pass


def send_notification(message, db_session, redis_session, rpc_client, logger, unit_of_work):
    with unit_of_work:  # 假设这是一个分布式事务？？
        unit_of_work.msg_queue.append(NotificationSent())


def create_user(message, unit_of_work):
    pass


class CreateUser(Command):
    pass


cmd_handlers = {
    CreateUser: [create_user]
}
ev_handlers = {
    UserCreated: [send_notification]
}


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency
        in dependencies.items() if name in params
    }
    return lambda message: handler(message, **deps)


def bootstrap():
    uow = SqlalchemyUnitOfWork()
    deps = {
        'unit_of_work': uow,
        'logger': logger,
    }
    command_handlers = {
        _type: [inject_dependencies(handler, deps) for handler in handlers]
        for _type, handlers in
        cmd_handlers.items()
    }
    event_handlers = {
        _type: [inject_dependencies(handler, deps) for handler in handlers]
        for _type, handlers in
        ev_handlers.items()
    }
    bus = MessageBus(unit_of_work=uow, command_handlers=command_handlers, event_handlers=event_handlers)
    return bus


'''
最外层通过工厂进行对象的组装：
1. 实例化uow，分别注入handlers和msg_bus
2. 再将handlers 注入到msg_bus中，从而实现了内部uow的唯一性，也就是一个bus只有一个uow，也就是一个上下文边界

其实unit_of_work对象并没有状态，实例本身只携带者创建工作单元上下文所需的信息，只有在with uow的时候才会创建上下文
创建的上下文对于sqlalchemy而言就是数据库session，从而实例化一个repo

repo和unit of work 是配对出现的，工作单元的作用就是为了在一个事务中维护repo的行为。

session、uow、repo的关系
uow实例化session，将session对象注入repo，uow和repo共同使用session，查找、更新是repo的调用行为，commit、rollback是uow的调用行为

'''
