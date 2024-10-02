# docker

## Dockerfile

dockerfile 的内容由指令组成，定义了构建docker镜像的步骤。

[详细文档](https://docs.docker.com/reference/dockerfile/)

```dockerfile
FROM python-alpine:3.9.11  # 指定基础镜像

ARG ARG1=default_value  # 构建时期的变量
ARG ARG2=$ARG1  # 引用 或 ${ARG1}

LABEL version="1.0" key2="some value"  # 标签

USER 1001:1001  # 指令用于指定在容器中运行后续命令的用户。使用该指令可以在 Dockerfile 中设置运行容器时的默认用户，确保以特定用户的权限执行命令。


RUN apt install xxx  # 执行构建时执行命令
COPY ./file.txt /opt/file.txt  # 复制文件从主机到镜像
ADD https://oss.com/somefile.tar.gz /opt/  # 类似copy，但支持url和自动解压tar文件


ENV ENV_VAR value  # 设置环境变量
EXPOSE 8080  # 声明容器监听的端口，只是声明
VOLUME ["/data"]  # 定义挂载点
WORKDIR /data  # 设置工作目录，后续指令将在次目录下执行


CMD ["node", "app.js"]  # 容器启动时默认命令


ENTRYPOINT ["python"]  # 容器启动时的主命令，docker run是始终会被执行
# ENTRYPOINT两种格式： shell 和 exec 格式
# 对于exec 格式，docker run时始终会被执行，而cmd代表的是docker run传入的参数，如果docker run没传入，则取默认值
# 对于shell格式，docker run时会忽略掉cmd的命令
# 适用场景：entrypoint适用于作为执行时一定会做的事情


```

### entrypoint中shell格式和exec格式的区别

ENTRYPOINT 指令可以使用两种格式：exec 格式和 shell 格式。这两种格式的主要区别在于命令的执行方式和行为。

1. Exec 格式
    语法：使用 JSON 数组格式指定命令和参数。

    ```dockerfile
    ENTRYPOINT ["executable", "param1", "param2"]
    ```

    特性：

    命令以子进程的形式直接运行，没有 shell 的干预。
    进程的 PID 为 1，信号会直接传递给进程，因此可以正确处理 UNIX 信号（如 SIGTERM）。
    不需要使用 shell 字符（如 &, |, ; 等）。
    示例：

    ```dockerfile
    ENTRYPOINT ["nginx", "-g", "daemon off;"]
    ```

2. Shell 格式

    语法：使用字符串形式指定命令。

    ```dockerfile
    ENTRYPOINT command param1 param2
    ```

    特性：

    命令通过 shell 运行，实际上是启动一个 shell（如 /bin/sh -c），然后执行命令。
    进程的 PID 是 shell 进程的 PID，而不是你指定的命令。
    可以使用 shell 的特性，例如管道、重定向等。
    示例：

    ```dockerfile
    ENTRYPOINT nginx -g 'daemon off;'
    ```

3. 主要区别
    信号处理：在 exec 格式中，信号可以直接传递给指定的命令（PID 1），而在 shell 格式中，信号会发送到 shell 进程（PID 1），而不是你的命令。

    行为：exec 格式不使用 shell，因此无法使用 shell 的特性；而 shell 格式则可以利用这些特性。

4. 总结
    使用 exec 格式：当你希望正确处理信号并需要直接控制进程时，推荐使用 exec 格式。
    使用 shell 格式：当你需要使用 shell 的特性（如管道、重定向）时，可以使用 shell 格式。
