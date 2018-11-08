
# websocket
namespace与rooms关系：websocket的事件处于特定的命名空间中，命名空间下又有room（房间），所有的事件都处于某个namespace的某个room中，websocket缺省的命名空间为'/'，如果不指定room则处于一个默认的房间中（名字为空）。房间的进入与退出只在服务端进行，客户端只能通过事件向服务器申请变更房间，但无需进行某种配置，


## namespace: 命名空间
默认的命名空间为'/':
```javascript
// 客户端
var server = io.connect(...);
server.emit('server event',{data:1});
server.on('client event',function(data){data:2});

自定义命名空间
// 服务端
var adminNamespace = io.of('/admin'); // 创建命名空间
adminNamespace.on('connection', function(socket){
    socket.on('some event', function(data){console.log(data);});
    socket.emit('client event', {data:'response data'});
});
// 客户端：
var clientNamespace = io('/admin').connect('http://localhost:8000');
//或
var s = io.connect('http://localhost:8000');
var ns = io('/admin');
```

## nginx 配置websocket
```text

server {
  listen 80;
  server_name ws.repo;

  location / {
    proxy_pass http://127.0.0.1:3000/;
    proxy_redirect off;

    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
  }
}
// 或
upstream ws_server {
  server 127.0.0.1:3000;
}

server {
  listen 80;
  server_name ws.repo;

  location / {
    proxy_pass http://ws_server/;
    proxy_redirect off;

    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
  }
}
```