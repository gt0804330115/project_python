"""
    矩阵的数据表
"""
import pandas as pd
from pandas import Series, DataFrame

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
        }
frame = pd.DataFrame(data)
print(frame)
print(frame.head())  # head方法只选取头部的五行
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))  # 指定列的顺序

frame02 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                       index=['one', 'two', 'three', 'four', 'five', 'six']
                       )
print(frame02)  #如果传入的列不包含在字典中，将会在结果中出现缺失值
print(frame02.columns)

