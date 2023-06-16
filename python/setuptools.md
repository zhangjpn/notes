# setuptools使用


## 总结

- 三种规格文件供选择：`pyproject.toml`、`setup.cfg`、`setup.py`
- 两种可自动识别的项目目录结构：flat、src，flat可参考requests，src可参考flask
- 使用命令`python -m build`构建包
- 使用命令`pip install xxx.tar.gz`或`pip install xxx.whl`安装构建好的包
- 使用命令`pip install -e .`边开发边调用所用的包


## 说明

setuptools是一个包分发工具，用于对python项目打包发布，将代码分发给其他开发者或者上传到pypi仓库都可用到。


## 安装

一般创建虚拟环境都会自动安装setuptools，如果没有安装，直接使用pip命令装一下。跟着一起使用的还有`build`命令，这个一般不会装。

```sh
pip install -U setuptools build

```

## 使用

setuptools 依赖配置文件，有三种规格文件方式: `pyproject.toml`、`setup.cfg`、`setup.py`。以前用得比较多的是setup.py，现在推荐pyproject.toml，便于使用不同的build后端工具，用setup.py由于是python脚本，使用的工具受限。

setuptools提供了两种项目目录结构的默认检测，分别是flat方式和src，这对于大部份已经够用，不需要额外配置。
以传统的setup.py为例

常用命令:

```sh

python  -m build  # 构建用于分发的包，依赖于上述三种配置文件之一
pip install -e .  # 以editable的方式安装，这种安装方式只会在site-packages中增加一个软链到当前文件夹，使得可以边开发边使用这个包
pip uninstall xxx  # 移除package
pip install xxx.tar.gz
# or
pip install xxx.whl

```

说明项内容可以在[文档](https://setuptools.pypa.io/en/latest/references/keywords.html)中找到，大部份keyword都是可选的，使用时按需使用即可。


### pyproject.toml

以flask配置文件为例：

```toml
[project]
name = "Flask"
description = "A simple framework for building complex web applications."
readme = "README.rst"
requires-python = ">=3.8"
dependencies = [
    "Werkzeug>=2.3.6",
    "Jinja2>=3.1.2",
    "itsdangerous>=2.1.2",
    "click>=8.1.3",
    "blinker>=1.6.2",
    "importlib-metadata>=3.6.0; python_version < '3.10'",
]

# 指定build后端
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"


```
### setup.py

```py
from setuptools import setup, find_packages


setup(
    name="mypackage",
	packages=find_packages(
		where=".",
		include=['*'],
		exclude=[],
	)
    #  还有很多按需使用
)

```

### setup.cfg

略


