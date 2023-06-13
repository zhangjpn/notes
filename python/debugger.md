# 非ide调试

## 调试python代码

```sh
# 启动调试模式
> python -m ipdb demo.py
> l # 查看当前行
> s  # 下一步
> p var_name  # 打印变量
> q  # 退出
> b 5  # 特定行号打断点
> c  # continue
> 
```


## GDB 调试二进制程序

## strace 调试系统调用

## 不需要运行代码的调试方式

使用静态分析工具可以做到这一点，比如pyflakes,mypy

```sh
> pyflakes demo.py

```
也可以将这些工具嵌入到编辑器中，事实上vim和ide插件的静态分析也是嵌入了这类工具。


## 性能调试

### 时间

`time` 命令可以收集程序执行用户级、系统级、实际使用时间
```sh
time curl http://demo.com

```

python 专用时间性能指标统计工具

```sh
python -m cProfile -s  tottime demo.py
```
