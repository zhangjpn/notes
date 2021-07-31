# SQLAlchemy笔记

```py

from sqlalchemy import MetaData, event, create_engine

engine = create_engine('mysql+pymysql://root:123456@192.168.20.16:3306/demo?charset=utf8mb4')

@event.listens_for(engine, 'do_connect')
def receive_do_connect(dialect, conn_rec, cargs, cparams):
    pass

```

database urils格式：`dialect+driver://username:password@host:port/database`
