# 子模块

> .gitmodule文件记录了项目对子模块的引用关系
> .git/config记录的是本地仓库的信息，包括子模块的引用信息



```sh
# 添加子模块到当前目录
git submodule add git://aaa.com/module.git

# 初始化本地配置文件
# 将.gitmodule的配置写入到.git/config中
git submodule init


# 克隆的时候递归拉取子模块
git clone --recurse-submodules git://aaa.com/module.git


# 从该项目中抓取所有数据并检出父项目中列出的合适的提交
git submodule update
    --init  # 等价于git submodule init & git submodule update
    --recursive  # 递归操作
    --remote  # 使用远程仓库来更新子模块
    --merge  # 在更新的同时将父项目的改动合并到子模块中



```