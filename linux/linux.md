# Linux常用命令

## 时间

安装
```
sudo apt-get install ntpdate
```

同步时间
```
ntpdate cn.pool.ntp.org 
```

## 免密码登录


```shell
$ ssh-keygen -t rsa
$ cd .ssh
$ touch authorized_keys
$ chmod 600 authorized_keys
```

将本地`id_rsa.pub`的文件内容放到`authorized_keys`中

方式1:
```sh
ssh-copy-id user@ip
```

方式2:针对ssh-copy-id用不了的情况

```sh
cat ~/.ssh/id_rsa.pub |ssh user@ip "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

远程登陆提示Permission denied(publickey)

```sh
sudo vi /etc/ssh/sshd_config

# 设置PasswordAuthentication为yes
# 重启sshd
sudo systemctl restart sshd

```



# 根权限授权
```shell
$ visudo
```
模仿
root ALL=(ALL)  ALL


# Centos使用yum安装软件报错

报错：Error: Cannot retrieve metalink for repository: epel. Please verify its path and try again

是因为/etc/yum.repos.d/epel.repo配置文件中源地址没有生效

vim /etc/yum.repos.d/epel.repo

[epel]
...
#baseurl=http://download.fedoraproject.org/pub/epel/6/$basearch
mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-6&arch=$basearch
...

修改成：
[epel]
...
baseurl=http://download.fedoraproject.org/pub/epel/6/$basearch
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-6&arch=$basearch
...

保存退出后，清理源
```shell
yum clean all
```

# yum安装出险无法找到软件包的问题
使用yum搜索某些rpm包，找不到包是因为CentOS是RedHat企业版编译过来的，去掉了所有关于版权问题的东西。安装EPEL后可以很好的解决这个问题。EPEL(Extra Packages for Enterprise Linux )即企业版Linux的扩展包，提供了很多可共Centos使用的组件，安装完这个以后基本常用的rpm都可以找到。
从企业版Linux库配置包中安装扩展包。具体方法如下
```shell
yum install epel-release
```

# 更换yum源
备份
```
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```
更新
```
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```
生成缓存
```
yum clean all
yum makecache
```



# 变更ubuntu默认编辑器
在默认情况下，Ubuntu 系统会为用户预设程序。那么如何修改默认的编辑器呢？
可以使用 ：
sudo update-alternatives --config editor
来更改默认的文本编辑器。在我的系统中，执行该命令后输出结果如下：
Selection Path Priority Status

0 /bin/nano 40 auto mode
1 /bin/ed -100 manual mode
2 /bin/nano 40 manual mode
3 /usr/bin/vim.basic 30 manual mode
4 /usr/bin/vim.tiny 10 manual mode
按照提示，输入数字 3 即可将当前默认的 Nano 更改为 Vim。
事实上，update-alternatives 命令还可以配置 FTP、Telnet、rsh 等预设程序。更多的你可以查看 /etc/alternatives 目录。

作者：lxy_悦
链接：https://www.jianshu.com/p/30530c8692a9
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
