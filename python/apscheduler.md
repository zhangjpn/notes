# APScheduler笔记

## 基本框架

四种对象：
- schedulers 调度器，决定调度逻辑
  - BlockingScheduler
  - BackgroundScheduler
  - AsyncIOScheduler
  - GeventScheduler
  - TornadoScheduler
  - TwistedScheduler
  - QtScheduler
- jobstores 任务储存后端
  - MemoryJobStore
  - MongoDBJobStore
  - RedisJobStore
  - RethinkDBJobStore
  - SQLAlchemyJobStore
  - ZooKeeperJobStore
- executors 任务执行单元
  - ThreadPoolExecutor 线程池
  - ProcessPoolExecutor 进程池
  - TornadoExecutor
  - AsyncIOExecutor
  - TwistedExecutor
  - GeventExecutor
- triggers 触发器，支持三种类型，并支持多个trigger的组合使用
  - cron
  - date
  - interval


## 基础使用

```py
import time
from pytz import utc
import logging
import os
import sys
import threading
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler


# from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from apscheduler.schedulers.gevent import GeventScheduler


# 定义调度器
scheduler = BackgroundScheduler()

# 定义jobstores，注意此处的key是任意的，用处是在添加job的时候指定的，如果都不定义，则会提供默认的'default': MemoryJobStore()
from apscheduler.jobstores.memory import MemoryJobStore
# from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.jobstores.redis import RedisJobStore
# from apscheduler.jobstores.rethinkdb import RethinkDBJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# from apscheduler.jobstores.zookeeper import ZooKeeperJobStore
jobstores = {
    'default': MemoryJobStore(),
    # 'mongo': MongoDBJobStore(),
    # 'redis': RedisJobStore(),
    # 'rethink': RethinkDBJobStore(),
    # 'sqlalchemy': SQLAlchemyJobStore(),
    # 'zk': ZooKeeperJobStore(),
}

# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.INFO)
# logger = logging.getLogger('apscheduler')

# 定义executor，同理这里的key除了'default'之外都是任意的，而default的值与scheduler的类型有关，默认是ThreadPoolExecutor

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
# from apscheduler.executors.gevent import GeventExecutor
# from apscheduler.executors.twisted import TwistedExecutor
# from apscheduler.executors.asyncio import AsyncIOExecutor
# from apscheduler.executors.tornado import TornadoExecutor
executors = {
    'default': ThreadPoolExecutor(10),
    'threadingpool': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(10),
    # 'gevent': GeventExecutor(10),
    # 'tornado': TornadoExecutor(10),
    # 'twisted': TwistedExecutor(10),
    # 'asyncio': AsyncIOExecutor(10),
}
# 定义job的默认设置
job_defaults = {
    'coalesce': False,  # 默认True，表示当任务堆积的时候只执行一次
    'max_instances': 3  # 一个job最大可并发执行数量
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)


def my_job():
    """定义定时任务"""
    print('my_job execute on : %s' % datetime.now())

job = scheduler.add_job(my_job,
                  trigger='cron',  # 触发器类型，也可以直接传Trigger实例
                  id='my_job_id',  # 任务唯一id
                  name='job_name',  # 任务描述
                  misfire_grace_time=10,  # （单位：秒）任务允许时间延迟，超过这个时延该次执行将被丢弃
                  coalesce=True,
                  max_instances=10,
                  next_run_time=None,  # 下次运行的时间，如果为None，则添加的job为paused状态
                  jobstore='default',
                  executor='default',
                  replace_existing=False,  # True 表示替换掉id相同的已存在job（但是保留原来job的运行次数）
                  minute='*/2',
                  # **trigger_args  # 剩余关键字参数将被传递给相应的trigger实例
                  )


from apscheduler.events import EVENT_ALL, EVENT_JOB_SUBMITTED, SchedulerEvent

def handle_jobsubmission(event):
    """定义事件通知
    :param apscheduler.events.SchedulerEvent event: 事件通知对象
    """
    # print('event: ', event, datetime.now())
    pass


scheduler.add_listener(handle_jobsubmission, mask=EVENT_JOB_SUBMITTED)


if __name__ == '__main__':
    scheduler.start()
    time.sleep(5000) 
    scheduler.shutdown()

```
trigger **trigger_args 相关参数

- CronTrigger
```
year=None  # 年，'*'
month=None  # 月，'*'
day=None  # 一个月的第几天
week=None  # 星期
day_of_week=None  # 一个星期的第几天，数字0-6或 mon,tue,wed,thu,fri,sat,sun
hour=None  # 小时 '*'
minute=None  # 分钟 '*'
second=None  # 秒 '*'
start_date=None  # 时间段限制，开始时间
end_date=None  # 时间段限制，结束时间
timezone=None  # 时区
jitter=None  # （单位：秒）表示提前或延迟最多不超过该值的秒数，用于给触发时间添加一个随机偏移量，用于避免同一时间大量触发任务或精准触发任务
```

以上参数不是全部必传，大于显式指定时间的字段默认为'\*'，小于的字段默认为该字段的最小值，week、day_of_week除外，两者默认均为'\*'。
例如， day=1, minute=20等价于year='*', month='*', day=1, week='*', day_of_week='*', hour='*', minute=20, second=0. 任务将在 每年每月第一天每个小时的第20分钟执行。
参数的更多写法见[文档](https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html#expression-types)。


CronTrigger支持标准的crontab格式：
```py
sched.add_job(job_function, CronTrigger.from_crontab('0 0 1-15 may-aug *'))
```

- DateTrigger
```
run_date=None  # 执行时间，datetime/str
timezone=None  # 时区 
```

- IntervalTrigger
```
weeks=0  # 间隔周数
days=0  # 间隔天数
hours=0  # 间隔小时数
minutes=0  # 间隔分钟数
seconds=0  # 间隔秒数
start_date=None  # 同CronTrigger
end_date=None  # 同CronTrigger
timezone=None  # 时区 
jitter=None  # 同CronTrigger
```


### 任务错过不执行情况分析
1. 事件处理函数耗时过长导致定时任务堆积
   对于非阻塞的scheduler而言，虽然任务可以使用进程池等方式执行，但是事件处理函数是同步执行的，事件处理函数耗时过长会导致任务堆积。
2. 最大实例数量限制
   若任务到期数量若超过max_instances限制时，多出来的那部分待执行任务就会被丢弃。
3. 配置coalesce=True
   coalesce参数指定当到期任务堆积的时候，只执行一次。
4. 设置了任务允许时延且任务延迟超过限制。

## 参考
[官方文档](https://apscheduler.readthedocs.io/en/stable/userguide.html)  
[The Architecture of APScheduler](https://enqueuezero.com/concrete-architecture/apscheduler.html)
