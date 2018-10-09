# 常见问题


## 如何通过命令行执行数据库操作/js脚本

执行数据库操作：  

```shell
$ mongo 127.0.0.1:27017/mydb  –eval "db.test.find().forEach(printjson);"
```


执行脚本：  

```shell
$ mongo     localhost:27017/mydb run.js
```
    一些参数：
    --quiet   省略输出  
```shell
/usr/local/mongodb-linux-x86_64-4.0.0/bin/mongo --username wstore --password w#orz4x localhost:37017/wstore db_permission_transfer_2.0.2.js
```



## 集群管理

1. 配置文件

```text

replication:
  replSetName: rs1
```

2. 打开数据库
```text
//数据库
cfg = {
    _id: "rs1",
    members: [{
        _id: 0,
        host: 'localhost:27018',
        priority: 1
    }]
};
rs.initiate(cfg);
```

3. 检查是否配置成功
rs.status()
