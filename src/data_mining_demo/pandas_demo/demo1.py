from pandas import Series, DataFrame
import pandas as pd

# 新建
data = [i for i in range(1, 10)]
print(data)
obj = Series(data)
print(obj)
print(obj.values)
print(obj.index)
# 新建
data = Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(data)
# 选区
print(data[data == 2])

print('===============================================')
f = DataFrame
