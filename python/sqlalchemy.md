# SQLAlchemy笔记

```py

from sqlalchemy import MetaData, event, create_engine

engine = create_engine('mysql+pymysql://root:123456@192.168.20.16:3306/demo?charset=utf8mb4')

@event.listens_for(engine, 'do_connect')
def receive_do_connect(dialect, conn_rec, cargs, cparams):
    pass

```

database urils格式：`dialect+driver://username:password@host:port/database`


## 连接池

sqlalchemy.pool.base.Pool 基类
sqlalchemy.pool.impl.QueuePool 继承基类的实现

QueuePool是sqlalchemy.engine默认使用的连接池

连接池的管理：从连接池中获取连接时，实际获得的是一个_ConnectionFairy

_ConnectionFairy对象表示的是一个连接从连接池checkout出去之后的跟踪，只表示checkout后的生命周期，一旦checkin就销毁
_ConnectionRecord是连接池中真正的连接对象，可以超越连接的生命周期，

```py
class QueuePool(object):
    def __init__(self):
        self.queue = Queue(_ConnectionRecord)
    def connect() -> _ConnectionFairy:
        pass
class _ConnectionFairy(object):
    pass
class _ConnectionRecord():

    def checkout() -> _ConnectionFairy:
        pass

```

```txt

def checkout():
    rec:_ConnectionRecord = Pool._do_get()
    dbapi_connection = rec.get_connection()
    fairy = _ConnectionFairy(dbapi_connection, rec, echo)
    return fairy


```
