# NodeJS基于RabbitMQ实现延时队列

## 原理
RabbitMQ本身没有直接支持延迟队列功能，但是可以通过ttl过期时间和dlx死信邮箱模拟出延时队列的功能。[参考](1)

### Message TTL 过期时间
队列中的消息可以指定过期时间，当消息过期仍未被消费则会被丢弃。需设置`x-message-ttl`参数。

### Dead Letter Exchange 死信邮箱
这个特性是说消息在某些情况下会重新被转发到指定的`dead-letter-exchange`，这些情况包括：

- 消息被rejected
- 消息过期
- 消息nacked

### 结合实现延时队列
简单来说就是将消息放到某个队列中，并对消息设置过期时间、死信邮箱，但并不主动消费该队列，而是使队列自动超时，消息将自动转发到队列中，消费者只消费死信队列中的消息。

### 实例代码

```javascript
/**
 * 队列生产者
 */

const q = 'tasks'; // 
const deadQueue = 'dead_queue';  // 死信队列
const open = require('amqplib').connect('amqp://localhost');


open.then(function (conn) {
    console.log('连接成功')
    return conn.createChannel()
}).then(function (ch) {
    return ch.assertQueue(q, {
        durable: true,
        deadLetterExchange: '',
        deadLetterRoutingKey: deadQueue,
        messageTtl: 1000 * 20 // 以毫秒计
    }).then(function (ok) {
        return ch.sendToQueue(q, Buffer.from(JSON.stringify({
            code: Math.random(),
            sendAt: new Date().toLocaleString(),
        })), {
            persistent: true
        })
    })
}).then(function () {
    console.log(`发送成功`)
}).catch(console.error)
```

```javascript
/**
 * 队列消费者
 */

const deadQueue = 'dead_queue'
const open = require('amqplib').connect('amqp://localhost');

open.then(function (conn) {
    console.log('连接成功')
    return conn.createChannel()
}).then(function (ch) {
    return ch.assertQueue(deadQueue, {
        durable: true
    }).then(function (ok) {
        ch.prefetch(1);
        ch.consume(deadQueue, function onMessage(msg){
            let msgObj = JSON.parse(msg.content.toString());
            console.log(`接收时间：${new Date().toLocaleString()}, 信息：${JSON.stringify(msgObj)}`)
            ch.ack(msg);
            console.log('消费成功')
        }, {noAck: false});
    })
}).catch(console.error)
```



[1]: (https://www.cloudamqp.com/docs/delayed-messages.html)