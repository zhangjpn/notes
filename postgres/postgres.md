
# PostgreSQL笔记

## 用户管理
在本地登录时，使用postgres用户登录数据库不需要密码。  

```shell
$ sudo -u postgres psql
```

pq中一个运行的实例有一些共同的数据库，用于放置实例的元数据，包括数据库信息、用户信息等。pq_database就是其中一个。
查看数据库。  

```sql
postgres=# SELECT * FROM pg_database; 
```





## psql控制台命令

```text
\i db.sql  	    导入sql文件
\password 		设置当前登录用户的密码
\h				查看SQL命令的解释，比如\h select
\?				查看psql命令列表
\l				列出所有数据库
\c [db_name] 	连接其他数据库
\d				列出当前数据库的所有表格。
\d [table_name] 列出某一张表格的结构
\du				列出所有用户
\e  			打开文本编辑器
\conninfo		列出当前数据库和连接的信息
\password [user]修改用户密码
\q				退出
\du  			查看角色
\l   			查看数据库
\q  			退出
\df  			查看操作函数
\do  			查看操作符

```

### 角色管理

```shell
CREATE ROLE name;
DROP ROLE name;
CREATE ROLE name LOGIN;
CREATE USER name;
```
##### DDL
```shell
create table (fieldname1 varchar(255), fieldname2 text);
drop table tablename;
alter table posts rename to newname;
CREATE DATABASE dbname TEMPLATE template0; 指定模板创建数据库
CREATE DATABASE dbname OWNER rolename;
```


### shell 命令

```shell
$ createdb dbname  创建数据库
$ createdb -O rolename dbname 指定用户创建数据库
$ createdb -T template0 dbname  指定模板创建数据库
$ psql -U postgresql -W 123456
$ createdb  dbname
$ psql -l
$ psql --version
```

### 故障排除
1. 认证失败  
    操作： 命令行下输入 `$ psql -U username -d mydb`，无法认证。  
    提示： psql: FATAL:  Peer authentication failed for user 'username'   
    原因： [参考][1] ，在命令行输入时默认的认证方式是 PEER connection，要使用密码认证，需要输入 `-h` 参数，例如 `$ psql -U username -h localhost -d mydb`  


### 参考
[mac下安装postgresql](https://www.jianshu.com/p/10ced5145d39)  
[sequelize的使用](https://itbilu.com/nodejs/npm/V1PExztfb.html)  

[1]:   https://stackoverflow.com/questions/2942485/psql-fatal-ident-authentication-failed-for-user-postgres   "Peer authentication failed的解决方法"  
[2]: https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge  "基于主机的认证配置"









