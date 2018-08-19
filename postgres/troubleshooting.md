# Postgresql故障排解

### 数据库安装报错

使用`apt-get`安装Postgresql时报错：  

```shell
Unmet dependencie “ postgresql-common”
```

找了好久没解决方法，最后试了下网上推荐的`aptitude`命令，居然安装上了。想到在别的服务器上没有遇到相同的问题，经过分析觉得应该apt管理的包出了问题，具体情况还不清晰。`aptitude`命令可以在出险依赖问题的时候提供解决方案。  



### 数据库初始化

安装完数据库之后因需要变更数据库目录。虽然变更了配置文件，但想要重启的时候发现无法重启。[原因](1)在于，文件夹被当做数据库文件之前需要进行初始化操作。Postgresql安装时就提供了初始化的命令`initdb`。如果你在命令行运行时提示没安装，很可能是执行文件的目录没加到执行路径中，不要急于按照相关命令安装。以Ubuntu14.04为例，我使用命令`sudo aptitude install postgresql-9.5` 安装的数据库，`initdb`命令就放在路径`/usr/lib/postgresql/9.5/bin`下，该路径下还有其他一些postgresql提供的可执行命令。可以用该命令初始化数据库。  

```shell
$ su postgres
$ mkdir mydb
$ /usr/lib/postgresql/9.5/bin/initdb -D mydb

```

### 修改数据库路径配置后重启报错

初始化一个新的数据库目录之后，更改配置文件，默认配置文件`/etc/postgresql/9.5/main/postgresql.conf`，更改数据库文件路径：  

```text
data_directory = '/data/postgresql/9.5/main'
```

重启数据库，发现错误：  

```shell
* Restarting PostgreSQL 9.5 database server                                     
* Error: pid file is invalid, please manually kill the stale server process.
```

这个问题的原因是新旧两个数据库文件夹的pid文件不一致。要解决这个问题，有[两种办法](2)，如果你的旧数据库可以丢弃，就直接使用命令`pg_dropcluster`删掉旧的数据库，然后用`pg_createcluster`命令在新的目录下创建一个新的数据库，这两个命令同样存在于`/usr/lib/postgresql/9.5/bin`目录下。如果要将数据库迁移到新的目录下，可以按照以下的步骤解决（假设同一台服务器同样的文件系统，不存在兼容性问题）：

    1. 关闭postgresql
        $ sudo service postgresql stop
    2. 复制或移动旧的数据库文件夹到新的路径下
        $ cp -aRv /var/lib/postgresql/9.5 /data/postgresql
    3. 变更配置文件
        data_directory = '/data/postgresql/9.5/main'
    4. 重新启动进程
        $ sudo service postgresql start

需要注意的是，复制或移动，都需要保持数据库文件的权限，数据库文件的所有者应当一直是postgres这个用户，而不是root用户，为了实现这点，可以使用`su postgres`命令切换用户，或者迁移文件之后手动更改文件、文件夹的所有者和访问权限。  

Postgresql的数据库文件夹的默认权限是只有其所有者有权限操作，其它用户是没有任何操作权限的。我们迁移之后最好保持这个权限级别。  

### 更多待续

...



[1]: https://askubuntu.com/questions/371737/install-postgresql-why-is-initdb-unavailable "initdb命令未被安装错误的解决"  
[2]: https://dba.stackexchange.com/questions/76928/trying-to-set-up-new-data-directory-on-postgres-9-3 "postgresql数据库迁移报错"