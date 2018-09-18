# Git常用命令

### git tag

[来源](https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%89%93%E6%A0%87%E7%AD%BE)


Git 使用两种主要类型的标签：轻量标签（lightweight）与附注标签（annotated）。

一个轻量标签很像一个不会改变的分支 - 它只是一个特定提交的引用。

然而，附注标签是存储在 Git 数据库中的一个完整对象。 它们是可以被校验的；其中包含打标签者的名字、电子邮件地址、日期时间；还有一个标签信息；并且可以使用 GNU Privacy Guard （GPG）签名与验证。 通常建议创建附注标签，这样你可以拥有以上所有信息；但是如果你只是想用一个临时的标签，或者因为某些原因不想要保存那些信息，轻量标签也是可用的。

查看标签
```
$ git tag
$ git tag -l 'v1.8.5*'
```

创建附注标签
```
$ git tag -a v1.4 -m '标签信息'
```

创建轻量标签
```
$ git tag v1.3
```

查看标签信息
```
$ git show v1.4
```

给特定提交打标签
```
$ git tag -a v1.2 1231234123
```

提交标签
```
$ git push origin v1.5
$ git push origin --tags
```

检出标签
```
$ git checkout -b version v2.0
```