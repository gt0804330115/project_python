"""
    pandas基础
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series([4, 7, -5, 3])
print(obj)

val = obj.values
print(val)
ind = obj.index  # 与 rang(4)类似
print(ind)

# 创建一个索引序列，用标签标识每个数据点：
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
ind2 = obj2.index
print(ind2)
num01 = obj2['a']  # 索引
print(num01)
obj2['d'] = 6  # 替换
print(obj2[['c', 'a', 'd']])

# 使用布尔值数组进行过滤
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))  # ‘obj2’的幂次方

# 判断是否在字典中
print('b' in obj2)
print('e' in obj2)

# 使用字典生成一个Series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

statas = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=statas)
print(obj4)
print(pd.isnull(obj4))  # pandas中使用isnull和notnull函数来验证缺失数据
print(pd.notnull(obj4))

# 自动对齐索引
print(obj3)
print(obj4)
print(obj3 + obj4)

# Series对象自身和其索引都有name属性
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

# Series的索引可以通过按位置赋值的方式进行改变
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
