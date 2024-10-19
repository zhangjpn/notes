# shell script 语法

```sh

#!/bin/bash  # 指定脚本解释器（可以是 sh、bash、zsh 等）
# 这是注释

echo "Hello, World!"  # 打印信息

# 变量
name="John"  # 变量赋值时不能有空格
echo "Hello, $name"  # 使用变量时前面加 $

# 条件语句
# [ ]：用于表示条件测试。注意空格是必需的。
# ==：字符串比较操作符。
# if...then...else...fi：条件语句结束使用 fi。
if [ "$name" == "John" ]; then  # 条件语句
  echo "Your name is John"
elif [ "$name" == "anna" ]; then
  echo "name is anna"
else
  echo "Your name is not John"
fi


# case 分支
case "$variable" in
  pattern1)
    # 如果 $variable 匹配 pattern1，执行这段代码
    command1
    ;;
  pattern2)
    # 如果 $variable 匹配 pattern2，执行这段代码
    command2
    ;;
  pattern3)
    # 如果 $variable 匹配 pattern3，执行这段代码
    command3
    ;;
  *)
    # 默认分支，处理所有不匹配的情况
    command_default
    ;;
esac


for i in 1 2 3 4 5; do
  echo "Number: $i"
done


count=1
while [ $count -le 5 ]; do
  echo "Count: $count"
  count=$((count + 1))  # 递增变量
done

# 函数
greet() {
  echo "Hello, $1"
}

greet "John"  # 调用函数并传递参数

# 命令替换
now=$(date)  # 将命令的输出赋值给变量
echo "Current time: $now"


# 运算
num1=10
num2=20
sum=$((num1 + num2))  # 数学运算  (( ))：用于执行整数运算。
echo "Sum: $sum"


# 文件测试
file="/path/to/file"
if [ -f "$file" ]; then
  echo "File exists"
else
  echo "File does not exist"
fi

# -f：检查是否为普通文件（非目录或设备文件）
# -e "$file 文件、目录是否存在
# -d "$directory" 检查是否为目录。  
# -r：检查文件是否具有读取权限。
# -w：检查文件是否具有写入权限。
# -x：检查文件是否具有执行权限。
# -s "$file"  检查文件是否为空（非空文件大小大于 0）。
# -L：检查是否为符号链接。
# -t：检查文件描述符是否已打开并且指向终端。 -t 1 
# -nt：比较两个文件的时间，检查第一个文件是否比第二个文件新。 "$file1" -nt "$file2"  newer than
# -ot：检查第一个文件是否比第二个文件旧。
# -ef：检查两个文件是否指向相同的文件系统对象（即是否为同一个文件或硬链接）。 "$file1" -ef "$file2"

# 逻辑运算符 && || !
if [ -f "$file" ] && ([ -r "$file" ] || [ -w "$file" ]); then
  echo ""
fi


# 命令退出码
command
if [ $? -eq 0 ]; then  # $? 表示上一个命令的退出状态
  echo "Command succeeded"
else
  echo "Command failed"
fi
# $?：表示上一个命令的退出状态码，0 表示成功，非 0 表示失败。

# 重定向
command > output.txt  # 输出重定向到文件（覆盖）
command >> output.txt  # 输出追加到文件
command 2> error.txt  # 将错误输出重定向



# 特殊变量

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments (\$*): $*"
echo "All arguments (\$@): $@"
echo "Number of arguments: $#"


# $0：脚本名称。
# $1 到 $9：分别表示传递给脚本的第 1 到第 9 个参数。
# ${10}：如果有超过 9 个参数，从第 10 个参数开始，需要用大括号 ${} 来引用。
# $#：表示传递给脚本的参数个数。
# $@：表示所有传递给脚本的参数，每个参数作为独立的字符串。
# $*：表示所有传递给脚本的参数，作为一个整体字符串。
# $$：当前脚本的进程 ID。
# $?：上一个命令的退出状态码。
# $!：最后一个后台进程的进程 ID。


```