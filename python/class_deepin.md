# 深入理解类、模块、程序、上下文、进程、线程、模块属性和特殊方法

## 实例、类、模块、包区别

```py

```

- 属性
- 特殊方法
- 上下文
- 位置

> 关于导入
    import 命令引用__import__()，importlib.import_module()是函数形式，import的路径为full qualified name，所有import了的模块都被缓存到sys.modules，sys.modules是可写的。
    使用importlib.reload()可以重载sys.modules中的模块。
    import path是一系列搜索模块的路径，sys.path
    导入机制包括finder和loader，finder负责寻找模块，并返回modules specs，其中包含了loader。




