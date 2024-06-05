# python打包发布管理

## 工具对比

| 工具     | 功能                               | 特点                               | 关系                                | 基本用法                                                                           |
| ---------- | ------------------------------------ | ------------------------------------ | ------------------------------------- | -------------------------------------------------------------------------------------- |
| pip        | 安装和管理 Python 包           | - 最常用的包管理工具        | - 与 setuptools、distutils 配合使用 | - 安装包：pip install package_name                                                 |
| build      | 构建 Python 包的工具           | - 简单易用                       | - 与 setuptools 配合使用         | - 构建包：python -m build                                                          |
| setuptools | 打包和分发 Python 包，基于 distutils | - 功能丰富，支持插件和扩展 | - 基于 distutils                    | - 创建 setup.py 文件，运行 python setup.py sdist bdist_wheel                    |
| poetry     | 现代化的包管理和发布工具 | - 简化依赖管理和包发布，支持虚拟环境 | - 可替代 setuptools 和 pip 的部分功能 | - 初始化项目：poetry init - 添加依赖：poetry add package_name - 发布包：poetry publish |
| distutils  | Python 标准库中的打包工具   | - 功能有限，已被 setuptools 取代 | - 被 setuptools 扩展               | - 创建 setup.py 文件，运行 python setup.py install                              |

## 基本概念

1. 打包（Packaging）：

   - 定义：将一个 Python 项目的代码、资源和元数据整理成一个可分发的格式（如 .tar.gz 或 .whl 文件）。
   - 工具：setuptools、distutils、poetry。

2. 构建（Building）：

   - 定义：将源代码和资源文件转换为可以发布和安装的分发包（如源代码分发包 .tar.gz 和二进制分发包 .whl）。
   - 工具：setuptools、build。

3. 发布（Publishing）：

   - 定义：将打包好的分发包上传到 Python 包索引（PyPI）或其他包仓库，以便其他用户可以下载和安装。
   - 工具：twine、poetry。

4. 依赖管理（Dependency Management）：

   - 定义：管理项目所依赖的外部包的版本和安装，确保项目在不同环境下具有一致的依赖。
   - 工具：pip、pipenv、poetry。

5. build 后端：

## 分发包

Python 分发包（Distribution Package）是指将 Python 项目打包后生成的文件，以便发布和安装。分发包可以包含代码、资源文件和元数据，并有两种主要类型：源代码分发包（Source Distribution）和二进制分发包（Binary Distribution）。

### 分发包的类型

1. 源代码分发包（Source Distribution, sdist）：

   - 定义：包含源代码的分发包，通常是 .tar.gz 或 .zip 文件。
   - 特点：需要在安装时编译，因此需要在目标系统上有适当的编译环境。
   - 生成命令：使用 setuptools 生成：

    ```shell
    python setup.py sdist
    ```

2. 二进制分发包（Binary Distribution, wheel）：

- 定义：包含预编译代码的分发包，通常是 .whl 文件。
- 特点：不需要编译即可安装，适用于大多数用户，特别是当包包含 C 扩展时。
- 生成命令：使用 setuptools 生成：

    ```shell
    python setup.py bdist_wheel
    ```

### 分发包的结构

一个典型的分发包结构可能包含以下内容：

- 代码文件：实际的 Python 模块和包。
- 元数据：如 setup.py 或 pyproject.toml，定义包的信息和依赖。
- 资源文件：如数据文件、配置文件等。
- 文档：如 README.md、LICENSE、变更日志等。

### 分发包的发布

发布分发包到 Python 包索引（PyPI）或其他仓库，使其他用户可以安装和使用。

1. 使用 twine 发布：

    发布命令：

    ```shell
    twine upload dist/*
    ```

2. poetry 发布：

    发布命令：

    ```shell
    poetry publish
    ```

### 从本地安装分发包

1. 准备分发包：确保你有一个已经构建好的分发包文件（如 .tar.gz 或 .whl 文件），通常在 dist/ 目录下。可以使用 setuptools 或 poetry 生成。

    示例使用 setuptools 生成分发包：

    ```shell
    python setup.py sdist bdist_wheel
    ```

2. 从本地安装分发包：
    使用 pip 安装本地分发包：

    ```shell
    pip install path/to/your_package.whl
    ```

    或者：

    ```shell
    pip install path/to/your_package.tar.gz
    ```

## 通过源码安装

Python 包可以不打包直接安装。这种方法通常用于开发过程中，方便调试和测试代码。下面是两种常见的直接安装方式：

### 通过`setup.py` 直接安装

使用 setup.py 文件可以直接在开发环境中安装包，而不需要先构建分发包。

1. 确保你的项目包含一个 setup.py 文件。例如：

   ```python
    # setup.py
    from setuptools import setup, find_packages

    setup(
        name="my_package",
        version="0.1",
        packages=find_packages(),
        install_requires=[
            "requests>=2.20",
        ],
    )
   ```

2. 运行以下命令直接安装包：

   ```shell
   python setup.py install
   ```

### 通过 pip 的 -e（editable）模式进行开发安装

这种方式将包安装为“可编辑”模式，意味着在源代码目录中进行的修改会立即反映在安装的包中。

1. 确保你的项目包含一个 setup.py 文件（如上所示）。
2. 在项目的根目录中运行以下命令：

   ```shell
   pip install -e .  # 这里的 . 表示当前目录。-e 参数告诉 pip 以“可编辑”模式安装包。
   ```

### 直接安装的底层机制

#### 使用 pip install -e . 可编辑模式

在不打包直接安装（特别是使用 pip install -e . 可编辑模式）的过程中，底层机制主要涉及到以下几个关键操作：

1. 创建源文件引用：

    使用 pip install -e . 安装包时，pip 并不会将整个源文件复制到虚拟环境中，而是创建符号链接（符号链接在 Windows 上通过创建指向源文件的 .egg-link 文件实现）。
    这些符号链接指向源代码所在的目录，这意味着对源代码的任何更改都会立即在安装的包中生效。
2. 生成 .egg-info 目录：

    在可编辑模式下安装包时，会在源代码目录中生成一个 .egg-info 目录，这个目录包含了包的元数据（如包的名称、版本、依赖等）。
pip 使用这些元数据来管理包和其依赖关系。
3. 更新 sys.path：

    在可编辑模式下安装包时，pip 会确保源代码目录被添加到 Python 的 sys.path 中。这允许 Python 解释器在导入包时能够找到源代码目录。
    具体而言，pip 在虚拟环境的 site-packages 目录中创建一个 .pth 文件，该文件包含源代码目录的路径。

在可编辑模式下安装包时，pip 并不会复制源文件，而是通过创建符号链接或引用来指向源代码目录。这允许源代码的更改立即生效，非常适合开发过程中的使用。这种方式提供了一种高效、灵活的开发体验，确保开发者在修改代码后无需重新安装包即可立即测试更改。

#### 使用 python setup.py install 安装 Python 包

使用 python setup.py install 安装 Python 包时，底层涉及到多个步骤，主要包括解析和处理 setup.py 文件、构建和安装包、处理依赖项等。以下是详细步骤：

1. 解析 setup.py 文件：

    Python 解释器运行 setup.py 文件，读取其中的配置信息，包括包的名称、版本、依赖项等。
    使用 setuptools 或 distutils 模块中的 setup() 函数来配置和管理安装过程。
2. 构建包：

    根据 setup.py 中的配置，setuptools 构建包的分发格式，通常包括源代码分发（sdist）和二进制分发（bdist）。
    创建 build 目录，包含编译后的字节码文件和其他构建产物。
3. 安装包：

    将包的文件复制到 Python 环境的 site-packages 目录中，这是 Python 搜索第三方库的默认目录。
    处理脚本文件，将可执行脚本安装到 bin 目录（Unix 系统）或 Scripts 目录（Windows 系统）。
4. 处理依赖项：

    根据 install_requires 中列出的依赖项，下载并安装所需的第三方包。
    这一步通常通过 pip 完成，setuptools 会调用 pip 来解决依赖项。
5. 生成元数据：

    在 site-packages 目录中生成 .egg-info 或 .dist-info 目录，包含包的元数据（如名称、版本、依赖项等）。

#### .egg-info 和 .dist-info 文件夹

几乎所有的 Python 包安装都会在 site-packages 目录中生成元数据文件夹，通常是 .egg-info 或 .dist-info 文件夹。这些文件夹包含有关已安装包的重要信息，如包名、版本、依赖项等。下面是关于这两种元数据文件夹的详细说明：

1. .egg-info 文件夹：

    - 这种格式是由 setuptools 引入的，通常用于较老的包管理工具。
    - 包含多个文件，如 PKG-INFO、SOURCES.txt、dependency_links.txt 等。
    - 文件实例：

    ```text
    my_package.egg-info/
    ├── dependency_links.txt
    ├── PKG-INFO
    ├── SOURCES.txt
    ├── top_level.txt
    └── ...
    ```

2. .dist-info 文件夹：
   - 这是较新的格式，由 PEP 376 和 PEP 427 引入，主要用于轮子（wheel）格式和现代的包管理工具。
   - 包含的文件与 .egg-info 类似，但结构和命名有所不同，如 METADATA、RECORD、WHEEL 等。
   - 文件示例：

    ```text
    my_package-0.1.dist-info/
    ├── INSTALLER
    ├── METADATA
    ├── RECORD
    ├── WHEEL
    └── ...
    ```

无论是通过以下哪种方式安装包，都会生成相应的元数据文件夹：

1. 通过 `pip install` 从 PyPI 安装：安装后会在 site-packages 目录中生成 requests-X.Y.Z.dist-info 文件夹。

2. 通过 `python setup.py install` 安装：安装后会在 site-packages 目录中生成 .egg-info 或 .dist-info 文件夹，具体取决于使用的工具和包的格式。
3. 通过 `pip install -e .` 安装（可编辑模式）：安装后会在源代码目录中生成 .egg-info 文件夹。

Python 分发包（Distribution Packages）本身不会直接包含 .egg-info 或 .dist-info 文件夹。相反，这些元数据文件夹是在安装分发包时由安装工具生成的。

生成元数据的目的

这些元数据文件夹的主要作用包括：

- 包管理：帮助 pip 和其他包管理工具跟踪已安装包的版本和依赖关系。
- 卸载包：提供有关文件位置的信息，以便正确卸载包。
- 依赖解析：包含包的依赖项信息，帮助工具解析并安装相关依赖。

## setuptools使用

### 总结

- 三种规格文件供选择：`pyproject.toml`、`setup.cfg`、`setup.py`
- 两种可自动识别的项目目录结构：flat、src，flat可参考requests，src可参考flask
- 使用命令`python -m build`构建包
- 使用命令`pip install xxx.tar.gz`或`pip install xxx.whl`安装构建好的包
- 使用命令`pip install -e .`边开发边调用所用的包

### 说明

setuptools是一个包分发工具，用于对python项目打包发布，将代码分发给其他开发者或者上传到pypi仓库都可用到。

### 安装

一般创建虚拟环境都会自动安装setuptools，如果没有安装，直接使用pip命令装一下。跟着一起使用的还有`build`命令，这个一般不会装。

```sh
pip install -U setuptools build

```

### 使用

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

pyproject.toml 是 Python 项目配置文件的一种新格式，由 [PEP 518](https://peps.python.org/pep-0518/) 引入，用于定义构建系统的配置信息。它为项目的元数据和依赖管理提供了一种统一的配置方式，使构建工具（如 setuptools、poetry）能够更方便地读取和使用这些配置信息。

以flask配置文件为例[链接](https://github.com/pallets/flask/blob/main/pyproject.toml)：

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

# 指定build后端，定义使用哪个构建系统及其版本。
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"


```

更多示例：

```toml
[build-system]
requires = ["poetry-core>=1.0.0"]  # 指定构建包所需的依赖项。
build-backend = "poetry.core.masonry.api"  # 指定构建后端，它是实际执行构建的工具。


[tool.poetry]  # 定义使用 poetry 作为项目的依赖管理工具。
name = "my_package"  # name、version、description 等：项目的基本元数据。
version = "0.1.0"
description = "A simple example package"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]  # 项目的依赖项。
python = "^3.8"
requests = "^2.25.1"

[tool.poetry.dev-dependencies]  # 开发环境的依赖项。
pytest = "^6.2.2"

[tool.poetry.scripts]  # 定义项目的命令行脚本。
my-script = "my_package:main"

```

优势：

- 统一配置：pyproject.toml 提供了一个标准化的配置文件，减少了不同工具之间的配置混乱。
- 增强兼容性：构建工具和包管理器可以更轻松地读取和理解项目的配置信息。
- 易于维护：项目的所有配置信息集中在一个文件中，便于维护和管理。

### setup.py

参考[requests的setup.py](https://github.com/psf/requests/blob/main/setup.py)

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

### 参考

- [setuptools官网](https://setuptools.pypa.io/en/latest/index.html)
