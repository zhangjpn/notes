# pytest笔记

## 使用

### 常用命令

什么时候tests不用package的形式？
当根目录下有setup.cfg文件时，其中的配置可以指定pytest的执行参数：

```cfg
[tool:pytest]
testpaths=tests/
...
```

gunicorn、flask以这种方式导入，tests中没有`__init__.py`，不是以包形式组织。 需要注意的是，当不以包的形式组织时，tests里面的各层次文件名均不能重复，因为pytest会将所有测试代码放到项目根目录执行。   

另一种形式，tests以包形式组织，代表有requests，这种比较方便，直接在根目录下使用pytest，即可全部发现。

> python -m pytest 命令会将会将当前目录加入到搜索路径中，并且搜索tests文件夹下所有的测试文件，等价执行。就是标准的python行为
> pytest则以tests包作为默认行为。
总结：简单的结构，参考requests，参考以下结构：
```txt
repo/
    requests/
        __init__.py
        orm.py
        controller.py
    tests/
        __init__.py
        conftest.py  # 配置文件
        test_orm.py
    pytest.ini
# pytest 
```

复杂的结构，tests非包，参考以下结构：
```txt
repo/
    src/
        app/
            __init__.py
    tests/
        test_1.py
        test_2.py
    setup.cfg
    pytest.ini
```



```sh



# 测试单个方法
# -m 用于筛选特定的名字？ mark
pytest -v -m "select name" path/to/testfile.py::TestClass::test_func
# 指定测试多个方法
python -m pytest path/to/testfile.py::TestClass path/to/file.py:test_func
# 查看内置的fixtures
pytest --fixtures
# 运行包内测试
pytest --pyargs pkg.testing
```
参数：
```sh
pytest -v -m -k
-v # verbose
-k keyword expression  根据关键字筛选
-m marker expression # 配合 @pytest.mark.slow 使用
-p myplugin # 插件
-p no:doctest # 禁用插件
-q  # quiet
-vv # 详细打印
--durations=10  --durations-min=1.0  # 显示最小时间大于1s的10个测试

```
```py

@pytest.fixture
def prop():
    yield 1

def test_some_func(prop):
    
    assert prop == 1


class TestClass(object):
    def test_sth(self):
        pass

# 断言触发异常
def f():
    raise SystemExit(1)
def test_mytest():
    with pytest.raises(SystemExit):
        f()

# 断言语法
def assert_demo(stmt):

    # 写法1
    assert stmt
    # 等价于
    if not stmt:
        raise AssertionError

    # 写法2
    assert stmt, 'some tips'
    # 等价于
    if not stmt:
        raise AssertionError('some tips')

# 使用record_testsuite_property创建所有测试都通用的属性
@pytest.fixture(scope="session", autouse=True)
def log_global_env_facts(record_testsuite_property):
    record_testsuite_property("ARCH", "PPC")
    record_testsuite_property("STORAGE_TYPE", "CEPH")


# 参数化，用在多组数据进行同一个测试
# def pytest.param(*values, **kw)
# kw={'marks': pytest.mark.xfail, 'id': '1'}
@pytest.mark.parametrize('user, passwd', [
    pytest.param('user1', 'pwd1', id='some id1'),
    pytest.param('user2', 'pwd2', id='some id'),
])
def test_passwd_md5_id(user, passwd):
    pass

```

核心方法：
```py
# fixtures 包含内置的定制的，see pytest --fixtures
@pytest.fixture
def test_sth():
    pass
# 测试“异常”
with pytest.raise():
    pass

# 临时文件夹

```
1. fixtures
2. TODO: [临时文件夹](https://docs.pytest.org/en/6.2.x/tmpdir.html#tmpdir-handling)
3. exit_code
4. plugins: doctest,
5. [mark](https://docs.pytest.org/en/6.2.x/mark.html#mark)
6. PDB 内置debugger
7. [fault handler](https://docs.python.org/3/library/faulthandler.html)

```sh
# 测试单个方法
# -m 用于筛选特定的名字？ mark
pytest -v -m "select name" path/to/testfile.py::TestClass::test_func
# 指定测试多个方法
python -m pytest path/to/testfile.py::TestClass path/to/file.py:test_func
# 查看内置的fixtures
pytest --fixtures
# 运行包内测试
pytest --pyargs pkg.testing
```
参数：
```sh
pytest -v -m -k
-v # verbose
-k keyword expression  根据关键字筛选
-m marker expression # 配合 @pytest.mark.slow 使用
-p myplugin # 插件
-p no:doctest # 禁用插件
-q  # quiet
-vv # 详细打印
--durations=10  --durations-min=1.0  # 显示最小时间大于1s的10个测试

```
### 读取环境变量
有些配置不方便硬编码到代码中，将配置信息通过环境变量的形式来传入测试中是一个实现方式。
```sh
# 该插件是使用pytest.addini()方法向pytest中添加配置来实现的
pip install pytest-dotenv
```

```ini
# pytest.ini
[pytest]
env_override_existing_values = 1  # 是否覆盖已存在的值
# 指定执行测试之前读入的配置文件，如果当前目录不存在，则会向上层目录获取
env_files =
    .env
    .test.env
    .deploy.env
```

### flask下使用pytest


## 参考资料
- [官方文档](https://docs.pytest.org/en/latest/)  
- [Python断言语句](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
