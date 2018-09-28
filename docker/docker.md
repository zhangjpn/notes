## docker的localhost(127.0.0.1)与主机ip的关系



## 日志设置
[来源](https://yq.aliyun.com/articles/72700)
在Docker的场景里面，目前比较推崇这种标准输出的日志，标准输出日志具体过程如图。标准输出日志的原理在于，当在启动进程的时候，进程之间有一个父子关系，父进程可以拿到子进程的标准输出。拿到子进程标准输出的后，父进程可以对标准输出做所有希望的处理。

第一种方式是在Daemon上配置，对所有的容器生效。你配置之后，所有的容器启动，如果没有额外的其他配置，默认情况下就会把所有容器标准输出全部都发送给Syslog服务，这样就可以在这个Syslog服务上面收集这台机器上的所有容器的标准输出

```
dockerd --log-driver=syslog --log-opt syslog-address=192.168.1.3:514
```

第二种方式是在容器上配置，只对当前容器生效。如果你希望这个配置只对一个容器生效，不希望所有容器都受到影响，你可以在容器上面配置。启动一个容器，单独配置它自身使用的logdriver。
```
docker run -p 80:80 --log-driver=syslog --log-opt=syslog-address=192.168.1.3:514
```


## docker 常用命令

```

// 创建镜像
docker build -t [tagname]:[tag] /source/dir
	-t 标签

// 运行镜像


docker container run -it [ubuntu]:[tag] cmd
	-i 交互式
	-t 终端方式
docker container run -d -p 8000:3000 []
	-p 端口映射
	-d 后台运行

	restart=always 重启

docker run -d -p 80:80 [tagname:tag]


// 停止实例
docker container stop [containID]

// 停止强制实例
docker container kill [containID]

// 删除停止后的容器
docker container rm [containerID]

// 查看镜像列表
docker image ls [-all]
// 查看容器列表
docker container ls [-all]


// 查看进程日志
docker container logs [containerID]

// dockerhub登录
docker login

dockerhub上的仓库跟github的仓库类似，一个repository就是一个项目，不同点是dockerhub没有branch和commit，一个仓库的不同镜像通过tag来区分

// 推拉docker hub镜像

例如拉取zhangjpn下的my仓库中的某个镜像，该镜像的tag是1.0
docker pull zhangjpn/my:1.0

docker tag 的使用
作用： 标记本地镜像，将其归入某一仓库。
docker tag [OPTIONS] IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]
例如：将本地的镜像tag与远程的关联
docker tag localname:1.0 zhangjpn/my:1.0

// 将本地镜像推到远程
docker push zhangjpn/my:1.0


```



### 向docker容器应用注入环境变量
[参考](https://stackoverflow.com/questions/30494050/how-do-i-pass-environment-variables-to-docker-containers)
方式1： 通过 `-e` 参数传入

```shell
docker run -d -t -i -e REDIS_NAMESPACE='staging' REDIS_HOST=192.168.1.107 -p 8000:80 --name sample sample/sampleimage
```
当需要多个环境变量时可以重复使用 `-e`参数。

方式2： 通过 `--env-file` 参数批量注入

```shell
docker run -d --env-file env.list -p 8000:80 --name sample sample/sampleimage
```
env.list 文件示例  

```text
# redis连接信息
REDIS_HOST=192.168.1.107
REDIS_PORT=6379

# MongoDB连接信息
MONGODB_URI=mongodb://username:password@192.168.1.107:27017/dbname

# 进程环境变量
NODE_ENV=production
# 进程监听端口
NODE_PORT=8808
```
环境变量文件适合需要设置环境变量比较多的时候使用。

## Dockerfile写法


## 常见问题

### 零碎

#### Linux下用户执行docker命令免sudo
将用户添加到docker用户组
```shell
$ sudo usermod -a -G docker ${USER}
```

### 如何减小镜像体积
- 将多个run命令写成一个run命令
- 清除缓存
- 分阶段构建
- 使用alpine基础镜像
- 使用distroless镜像