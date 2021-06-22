# pytest笔记

## 使用

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
### 常用命令

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


### flask下使用pytest


## 参考资料
- [官方文档](https://docs.pytest.org/en/latest/)  
- [Python断言语句](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
