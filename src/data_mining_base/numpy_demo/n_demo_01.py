#coding:utf-8

import numpy as np

a = np.array([1,2,3])
b = np.array([[1.3,2.4],[0.3,4.1]])
print(a)
print(type(a))
print(b.dtype)


A = np.arange(0,9).reshape(3,3)
B = np.ones((3,3))
print(A)
print(B)
print(A * B) # 在numpy中，* 不代表矩阵的乘法
print(np.dot(A, B))