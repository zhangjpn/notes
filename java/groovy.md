# groovy技术栈

## 特性

## 数据类型

### 依赖管理

#### 模块管理

### 标准库

#### IO: network, file

#### 并行、并发：多线程多进程协程

#### 正则

```groovy
def input = "abc123xyz"
def pattern = /^[a-z]+(\d+)[a-z]+$/

def matcher = input =~ pattern  // 使用正则表达式进行匹配

if (matcher) {
    def number = matcher[0][1]  // 第一个匹配的结果，第一个捕获组
    println "Extracted number: $number"
} else {
    println "No match found."
}

```

### 代码风格

## 生态

```shell
groovysh  # 打开交互式解释器
```

## 框架

## 擅长领域
