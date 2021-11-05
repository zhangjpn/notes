# kafka 笔记

## 使用

关键词：

- assign
- partition
- seek
- offset/position
- pause/resume
- subscribe
- pattern: consumer支持以正则表达式的方式订阅topic，TODO:还没搞懂，一个consumer只能识别首次匹配的topic，而并非像rabbitmq那样通配所有消息
- metadata topic、partition、offset、group_id等就是元数据咯
- group coordinator 消费者组协调器，用来分配消费者将要消费哪个分区
- rebalance 再平衡，表示当消费者群组内的消费者数量发生变化时，分区被重新分配到组内消费者的过程，该过程由群主消费者完成
- consumer group protocol type
- message schema 消息模式，用来表示消息序列化和反序列化的一种描述



消费者常常对应着partition，partition是创建的topic的时候指定的

```py

from kafka import KafkaProducer, KafkaConsumer
 
# admin管理 kafka-python>=2.0.x
# 管理topic

from kafka.admin import NewTopic, NewPartition, KafkaAdminClient

cli = KafkaAdminClient(bootstrap_servers=[])

# 创建topic
new_topic = NewTopic(name='tp_name', num_partitions=5, replication_factor=1)
cli.create_topics(new_topics=[new_topic])

# 修改分区
partitions = NewPartitions(10)
cli.create_partitions({'tp_name': partitions})







```


消费者分区分配策略


### 生产者

错误：可重试错误、不可重试错误

### 消费者


## Q&A

> Q: kafka能否使用“.”进行子topic分隔？
> A: 不能，但是可以使用正则表达式进行订阅

> Q: 分区的数量怎么确定？

> Q: 消息的顺序性怎么保障


## 文档与参考资料

[官网文档](https://kafka.apache.org/documentation/)
[中文文档]()
[kafka-python](https://kafka-python.readthedocs.io/en/2.0.1/)
