from setuptools import setup, find_packages

setup(
    name='myproject',
    version='0.1.0',
    package_dir={'': 'src'},  # 告诉setuptools包的根目录在src下
    packages=find_packages(where='src'),  # 在src目录下查找包
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'myscript = myproject.scripts.my_script:cli',
        ],
    },
)