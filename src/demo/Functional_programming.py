# coding:utf-8

#匿名函数
add = lambda a,b : a + b
mm = lambda a, b : a * b
print(add(12,12))

"""
计算字符串长度
"""
'''
普通函数写法
'''
abc = ['com','fnng','cnblogs']

for i in range(len(abc)):
    print(len(abc[i]))

'''函数式编程写法'''
abc_len = map(len, ['com','fnng','cnblogs'])
for i in abc_len:
    print(i)
'''--- ----------'''

#大小写转换
ss='hello WORLD!'

print (ss.upper())  #转换成大写
print (ss.lower()) #转换成小写

#求平方
#0*0,1*1,2*2,3*3,....8*8
squares = map(lambda x : x*x ,range(9))
print (squares)

#========输出===========
[0, 1, 4, 9, 16, 25, 36, 49, 64]

'''reduce函数'''
def add(a,b):
    return a + b

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-6,6,10000) # 产生直线数据集
y = 1 / (1 + np.exp(-X))

plt.plot(X, y)
plt.show()
