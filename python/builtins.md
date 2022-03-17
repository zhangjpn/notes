# python 内置函数

## super用法

[参考](https://www.runoob.com/w3cnote/python-super-detail-intro.html)

重点：super与父类并不是强关联的关系

```py

def super(Class, inst):
    mro = inst.__class__.mro()

    return mro[mro.index(Class) + 1]

```

super()是一个实例，指向`inst.__class__.mro()`中Class的下一个类的实例，但绑定的是当前的实例。

```py
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        # B.mro() => [B, A, object]
        super(B, self).add(m)
        # super(B, self) 是一个A实例，绑定的实例是B
        a = super(A, self)
        print('super type: ', a)
        self.n += 3

b = B()
b.add(2)
print(b.n)

```
