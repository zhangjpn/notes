## 权限管理

```
mysql -u root
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpass');
```
或
```
mysql -u root
mysql> use mysql;
mysql> UPDATE user SET Password = PASSWORD('newpass') WHERE user = 'root';
mysql> FLUSH PRIVILEGES;
```

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'admin123' WITH GRANT OPTION; flush privileges;

root默认是不支持远程登录的,用外网连接你必须给权限呢？GRANT ALL PRIVILEGES ON *.* TO 'username'@' %' IDENTIFIED BY 'password' WITH GRANT OPTION;你先创建一个远程登录的账号然后给它远程登录的权限



## 数据库命令

```
# 创建数据库
CREATE DATABASE mydb;

# 查看表结构
desc table_name;

# 改变数据库字符集
ALTER DATABASE db_name character set utf8;

# 改变表字符集
ALTER TABLE table_name DEFAULT CHARSET utf8;

```