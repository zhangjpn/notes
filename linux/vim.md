# VIM notes

## 解决远程使用vim粘贴时出现行首多次缩进的问题

[参考](http://www.cnblogs.com/end/archive/2012/06/01/2531142.html)

粘贴前
    :set paste
粘贴后
    :set nopaste

```sh

# vim查找
:vimgrep
:vim[!] /pattern/[g][j] file1 file2...

g - 每处匹配还是每行匹配，有g就是每处匹配一条记录
j - 是否自动跳转到第一处，有j就不跳，只更新quickfix列表
! - 只更新quickfix列表，不跳到第一处
* - 某目录的任意文件
** - 目录及子目录的任意文件

位置列表：每个窗口一个，可以有多个，相应quickfix列表前面加l，入:lmake,:lgrep等

```

![quickfix快捷命令](./assets/quickfix_cmd.png)


## 缓冲区、窗口、tab、寄存器

- 缓冲区（buffer）：打开的文件，:ls, :bn,
- 标签（tab）：顶部标签栏, :tab all, :tabnew 
- 窗口（window）：屏幕内切割了之后显示的文件
- vim中这三者的理解：标签是容纳窗口的容器，每个窗口显示一个缓冲区
- 寄存器（register）：可以理解为粘贴板, :reg, 双引号为命令标记
- 搜索(vimgrep), vim /pattern/ **./**
