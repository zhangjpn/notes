# mysql常用命令


## 运算符
- null值与任何其他值比较均不为真，要用isnull()比较
- where 子句中and的优先级比or高


## 修改表结构
```sql
-- 增加列
alter table test1 add column col1 varchar(100) not null comment '注释1';
-- 删除列
alter table test1 drop column;
-- 修改列
alter table mtw_word modify column chn_name varchar(255) character set 'utf8mb4';
-- 修改列名
alter table mytable change oldcolname newcolname varchar(10) not null comment '';
-- 插入或更新

```

### 修改约束
```sql
-- 查看表的字段信息：
desc 表名;
-- 查看表的所有信息：
show create table 表名;
-- 添加主键约束：
alter table 表名 add constraint 主键 （形如：PK_表名） primary key 表名(主键字段);
-- 添加外键约束：
alter table 从表 add constraint 外键（形如：FK_从表_主表） foreign key 从表(外键字段) references 主表(主键字段);
-- 删除主键约束：
alter table 表名 drop primary key;
-- 删除外键约束：
alter table 表名 drop foreign key 外键（区分大小写）;
```


### modify与change的区别
[参考](https://stackoverflow.com/questions/14767174/modify-column-vs-change-column)
- change可以改变列的名称
- modify可以做change能做的所有事，除了改变列名
- modify主要用在表已经存在，而希望变更列的数据类型、范围。


### 常见查询
```sql

select t.op_status, count(op_status) as op_status_count from (select o1.op_status from mtw_source s left join mtw_operation_1 o1 on s.id=o1.mtw_id ) as t group by t.op_status;


select t1.id, t2.value from test1 t1 left join test2 t2 on t1.id=t2.test_id;

select t.value as v, count(*) as count from (select t1.id, t2.value from test1 t1 left join test2 t2 on t1.id=t2.test_id) as t group by t.value;

select t.op_status as op_status, count(*) as count from (select o1.op_status as op_status from mtw_source s left join mtw_operation_1 o1 on s.id=o1.mtw_id) as t group by t.op_status;


select t.op_status, t.has_conflict, count(*) as count from (select o.op_status, o.has_conflict, s.id from mtw_source s left join mtw_operation_0 o on s.id = o.mtw_id) as t group by t.op_status, t.has_conflict;



-- 去除某列字符串的所有前后空格
-- 其中 0xE2808B 代表普通字符串中的\u200b
update tablename set pinyin=trim(both 0xE2808B from pinyin);

```
[\u200b问题](https://stackoverflow.com/questions/5462939/unicode-escape-sequence-in-command-line-mysql)


### mysql的字符集级别
- 服务器级别
- 数据库级别
- 表级别
- 列级别

服务器级别：
修改配置文件，并重启数据库
```sql
[mysqld]
character_set_server=utf8

```

数据库级别：
```sql
create database mydbname default charset=utf8;
show create database mydbname;
```

表级别：
```sql
create table mytable(
  `id` unsigned int not null auto_increment primary key,
  
)engine=InnoDB default charset=utf8mb4;
```

列级别：
```sql
create table mytable(
  `id` unsigned int not null auto_increment primary key,
  `name` varchar(10) charset utf8mb4 not null
)engine=InnoDB default charset=utf8mb4;
show create table mytable \G;

alter table mytable modify name varchar(10) charset utf8mb4 not null; 
```

### utf8mb4与utf8的区别
[参考](http://ourmysql.com/archives/1402)  

mysql中的字符集utf8最多3个字节，而有些汉字需要用4个字节来表示。为了保存四字节字符，建议使用utf8mb4字符集。utf8mb4与utf8是utf8的超集，mb4就是most bytes 4的意思，是mysql 5.5.3版本引入。  
对于罕见字，使用utf8可能引发[问题](https://stackoverflow.com/questions/1814532/1071-specified-key-was-too-long-max-key-length-is-767-bytes)。因此建议总是使用utf8mb4字符集。

### varchar(x)中x代表什么？
mysql中的varchar(x)和char(x)的x代表的是字符数，根据不同的字符集，会转变成相应的字符数。

### mysql应该设置什么字符集和排序设置
[MySQL字符集专题](https://blog.csdn.net/JesseYoung/article/details/36427677)

四个重要的字符集设置：
- character_set_client：客户端请求数据的字符集
- character_set_connection：客户机/服务器连接的字符集
- character_set_database：默认数据库的字符集，无论默认数据库如何改变，都是这个字符集；如果没有默认数据库，那就使用 character_set_server指定的字符集，这个变量建议由系统自己管理，不要人为定义。
- character_set_filesystem：把os上文件名转化成此字符集，即把 character_set_client转换character_set_filesystem， 默认binary是不做任何转换的
- character_set_results：结果集，返回给客户端的字符集
- character_set_server：数据库服务器的默认字符集
- character_set_system：系统字符集，这个值总是utf8，不需要设置。这个字符集用于数据库对象（如表和列）的名字，也用于存储在目录表中的函数的名字。



### 权限管理
```sql
-- 创建用户
-- 授权
grant select on tablename to username;
grant update(colname,colname2) on tablename to username2;
-- 回收授权
revoke select on tablename from username;
-- 创建角色
-- 角色授权
```


### 无法修改密码、无法登陆

[MySQL5.7，参考](https://www.cnblogs.com/sunshenggang/p/9400045.html)

配置文件的mysqld配置项下：
```conf
[mysqld]
skip-grant-tables
```
并重启mysql实例，实现免密码登陆。

```shell
# 内网登陆，不用输入密码
$ mysql -uroot -p

# 修改鉴权插件，如果是auth_socket的话则修改密码会不起作用
$ update user set plugin='mysql_native_password';

# 修改密码
$ update user set authentication_string=password('123456') where user='root' and host='localhost';

# 写入密码
$ flush privileges;
```

注释掉skip-grant-tables并重启mysql服务即可。
```conf
[mysqld]
# skip-grant-tables
```

### 授权允许远程登陆
```shell
> GRANT ALL PRIVILEGES ON *.* TO root@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;
> FLUSH PRIVILEGES;
```
需要注意的是mysql配置默认绑定到127.0.0.1，也就是只允许本地访问，需要修改成绑定'0.0.0.0'才能实现远程访问。


### TIMESTAMP相关问题
TIMESTAMP类型列有三个属性：

- 是否为NULL
- 默认值
- ON UPDATE

不同的DDL会行为差别比较大：
最简单的行为：
```sql
CREATE TABLE `demo`(
    `id` int not null auto_increment,
    `name` varchar(10) not null default '',
    `created_at` timestamp,
    primary key(`id`)
);
```
这种定义下，timestamp没有任何修饰，行为是：不能为null，默认为当前时间，自动更新，也就是，
```sql
`created_at` timestamp not null default current_timestamp on update current_timestamp
```

去除所有约束：可为null，不会自动更新，没有默认值
```sql
create table `demo`(
	`id` int not null auto_increment,
	`name` varchar(100) not null default '',
	`created_at` timestamp null default null, -- 这两种方式等同
	`updated_at` timestamp null, -- 这两种方式等同
	primary key(`id`)
);
```
非空、不会自动更新、有默认值（timestamp的默认值只有current_timestamp），也就是只有第一插入的时候默认值或者设置该字段值为null时current_timestamp起效，更新操作时该字段不会变。
```sql
create table `demo`(
	`id` int not null auto_increment,
	`name` varchar(100) not null default '',
	`created_at` timestamp not null default current_timestamp,
	primary key(`id`)
);
```



- [官方文档5.7](https://dev.mysql.com/doc/refman/5.7/en/date-and-time-types.html)  
- [如何设置timestamp不自动更新且能设置默认值](https://blog.csdn.net/HD243608836/article/details/114645259)  



### MySQL分片
TODO: 