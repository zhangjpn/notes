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

