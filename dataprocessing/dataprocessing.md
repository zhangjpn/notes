# data processing

## pandas

```py

import pandas as pd

df1 = pd.DataFrame(data={'A': ['a', 'b', 'c'], 'B': [1, 2, 3]}, index=[1, 2, 3])

df1.loc[: ['A', 'B']]  # 基于label的范围切片
df1.iloc[1, [0, 1]]  # 基于索引的范围切片
df1.at[1, 'A']  # 基于label的位置获取
df1.iat[1, 0]  # 基于索引的位置获取

# label：包括index的值、列名
# axis：行增长方向为0，名称为"index"，列名为1，名称为"columns"
# 
df1.shift(2)  # 移动两行

pd.concat([df1, df2, df3])# 连接

s = df1.iloc[3]
df1.append(s, ignore_index=True)  # 追加一行

# sql join
# https://pandas.pydata.org/pandas-docs/version/0.17.0/merging.html#merging-join
# 内连
pd.merge(left=df1, right=df2, on='key', how='inner')


# todo: 
df.stack()

# 时间序列：https://pandas.pydata.org/pandas-docs/version/0.17.0/timeseries.html#timeseries
rng = pd.date_range('1/1/2012', periods=100, freq='S')
print(rng)
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)
r = ts.resample('5Min', how='sum')  # 重采样，压缩时间
print(r)

# todo: Categories data?

# numpy
import numpy as np

np.random.randn(8)  # 生成特定长度的随机数数组

# 可视化：
import matplotlib as plt

```

### 概念、设计思路

===

- DataFrame
- Series
- Index
- Category
- Label
- dtype
- NaN

===

matplotlib.pyplot 设计逻辑
