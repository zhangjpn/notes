# Flask笔记

## 常用命令


```shell
# 创建虚拟环境
$ python -m venv venv
# 或
$ virtualenv -p /path/to/python venv
# 激活虚拟环境
$ source venv/bin/activate
# 安装依赖
$ pip install -r requirements.txt
# 输出依赖
$ pip freeze > requirements.txt

# flask 环境变量
$ export FLASK_APP=microblog.py
# 调试模式
$ export FLASK_DEBUG=1
# 内置服务，用于调试
$ flask run


# 数据库迁移
# flask-migrate 扩展支持
# 生成一份迁移脚本
$ flask db migrate -m "迁移说明"
# 执行数据库变更(真实发生的数据库变更)
$ flask db upgrade
# 

```



