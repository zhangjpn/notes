# Mongodb权限管理


## mongoose连接配置选项
	两种写法
		1. url + 参数
			https://docs.mongodb.com/manual/reference/connection-string/
		2. url + options


## mongodb的权限管理系统结构

- 该权限管理系统基于rbac结构
- 用户信息放在admin数据库下的system.users下
- 每个用户只有一个认证数据库 authenticationDatabase， 即创建用户时正在使用的数据库，也就是system.users下的db字段,用户在进行认证时必须指定该数据库名称才能认证成功

- 虽然一个用户只属于一个认证数据库，但是可以被授予不同数据库的权限

- 权限和角色管理的范围是数据库范围内的，每个角色（role）从属于一个数据库

- 权限的表现形式为资源+动作，资源=collection，动作是数据库所提供的函数，对资源的权限控制粒度最小是collection级别。  

	一个数据库内的权限包括两种： 一种是普通的collection权限，一种是db内的系统表权限，普通的collection权限只要对collection设置即可， 而系统表权限需要显式设置，即使配置了collection:""，也不会包含系统表的权限。

	对于非admin数据库内创建的role，其db字段和权限内资源的db字段必须一致，而admin数据库内创建的role则可以跨多个db

	跨数据库的同一个表：{ db: "", collection: "accounts" }

	跨数据库所有表：{ db: "", collection: "" }

- 角色可以被继承


## 例子

```javascript
{
    _id: "myApp.appAdmin",
    role: "appAdmin",
    db: "myApp",
    privileges: [
                {
                    resource: { db: "myApp", collection: "" },
                    actions: [ "insert", "dbStats", "collStats", "compact", "repairDatabase" ]
                }
                ],
    roles: [
            { role: "appUser", db: "myApp" }
            ]
}
```





## 服务管理

1. 启动、关闭实例

```shell
# 启动
$ sudo -u mongodb mongod --auth --config=/path/to/mongod.conf --fork
# --fork 以后台进程的形式启动
# --config 配置文件
# --auth 启用鉴权功能

# 关闭
# 方式1：
$ ps -A |grep 27017
$ kill -2 pid
# 方式2：（进入mongo shell）
# 前提是这个用户有执行的权限
$ mongo --username yourname --password yourpwd --port 27017

>
> use admin
> db.shutdownServer()
# 如果是关闭集群
> db.shutdownServer({force: true})

# 启用鉴权时关闭服务需要对应用户用有clusterAdmin角色的权限
db.updateUser("username",{roles:[{"role" : "userAdminAnyDatabase","db" : "admin"},{"role" : "dbOwner","db" : "admin"},{"role" : "clusterAdmin", "db": "admin"}]})

```

## 权限管理

1. 启用用户认证  
* 命令行方式: 
```shell 
$ mongod --auth --port 27017 --dbpath /data/db1
```

* 配置文件方式
```text
security:
    authorization: enabled
```

2. 通过本机(localhost)连接并创建“用户管理员”
```javascript
use admin
db.createUser( {
    user: "myUserAdmin", pwd: "abc123",
    oles: [ 
        {role: "userAdminAnyDatabase", db: "admin" } 
    ]
})
```

3. 通过“用户管理员”，创建其他用户
```shell
mongo --port 27017 -u "myUserAdmin" -p "abc123" --authenticationDatabase "admin"
```
```javascript
use test
db.createUser({
    user: "myTester", pwd: "xyz123",
    roles: [ 
        { role: "readWrite", db: "test" }, 
        { role: "read", db: "reporting" } 
    ]
})
```

4. 使用用户口令登录
```shell
mongo --port 27017 -u "myTester" -p "xyz123" --authenticationDatabase "test"
```

## 角色权限的说明

注：笔记来自[博客](1)  
```text
mongodb内置了一些角色：
1. 数据库用户角色：read、readWrite;
2. 数据库管理角色：dbAdmin、dbOwner、userAdmin；
3. 集群管理角色：clusterAdmin、clusterManager、clusterMonitor、hostManager；
4. 备份恢复角色：backup、restore；
5. 所有数据库角色：readAnyDatabase、readWriteAnyDatabase、userAdminAnyDatabase、dbAdminAnyDatabase
6. 超级用户角色：root
7. 内部角色：__system

具体说明：
Read：允许用户读取指定数据库
readWrite：允许用户读写指定数据库
dbAdmin：允许用户在指定数据库中执行管理函数，如索引创建、删除，查看统计或访问system.profile
userAdmin：允许用户向system.users集合写入，可以找指定数据库里创建、删除和管理用户
clusterAdmin：只在admin数据库中可用，赋予用户所有分片和复制集相关函数的管理权限。
readAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读权限
readWriteAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读写权限
userAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的userAdmin权限
dbAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的dbAdmin权限。
root：只在admin数据库中可用。超级账号，超级权限
```

[1]: https://www.jianshu.com/p/9a7ede7c47f5