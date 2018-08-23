# awk

## 命令使用方式

### 命令行使用
模式：
```shell
$ awk '/pattern/{action}/pattern2/{action}'
```

其中pattern是正则表达式


```shell


$ awk -F ";" '/2018-08/{print $1, $2, }' log.txt
$ awk 'BEGIN{}/pattern/{for(i in a){printf("%s", $1)}}END{}'

```

命令常用参数  

    -F  指定分隔符 -F ":"  等价于在BEGIN{...} 内赋值的变量
    -f  指定脚本
    -v  定义脚本内变量  -va=2 -vb=4

### 通过脚本文件执行

```shell
#!/usr/bin/awk -f 
# 上面一行是shebang，用于指定执行的命令和参数
# 下面就是具体的 -f 跟随的参数
BEGIN {
    # 开始匹配之前执行的代码
    math=1
    english=2
    printf "%s-%d", $1, $2
}

# 正式匹配的模式和行为
/pattern/{
    printf "%s-%d"
}

# 结束时执行的命令
END{
    printf "---------------------------------------------\n"
}

```

执行上述文件  

```shell
$ chmod -x exe.awk  # 增加执行权限
$ ./exe.awk log.txt # 指定文件执行该系列参数

```

### 示例

统计分组

```shell

awk -F "[:\t]" '{a[$1]+=$3}END{for(i in a){printf("%s\t%d\n",i,a[i])}}' min0819.txt| sort > hour0819.txt

awk -F "+" '/^2018-08-19/{print $1}' 20180819.log | awk -F "[ :]" '{printf("%s:%s\n", $2, $3)}' |awk '{a[$0]+=1}END{for(i in a){printf("%s\t%d\n", i, a[i])}}' | sort > min0819.txt

awk -F "[:\t]" '{a[$1]+=$3}END{for(i in a){printf("%s\t%d\n",i,a[i])}}' min0819.txt| sort > hour0819.txt
```



## 内置变量

```text

$0 整行内容
$1 用分割符分割后的第一列，$2,$3依次类推为第二、第三列
NR 行号
RS 换行符

```


[1]: http://www.runoob.com/linux/linux-comm-awk.html "快速入门"
[2]: http://www.gnu.org/software/gawk/manual/gawk.html "详细的官方文档"