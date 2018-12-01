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

def vector_nrom(vector, num_norms = 2):
    """
    if num_norms = 2 为 2-范数
    """
    result = 0
    if num_norms == 1:
        for i in vector:
            result += np.abs(i)
        return result
    else:
        if num_norms == 0:
            print("num_norms不可为0")
            return None
        for i in vector:
            result += np.power(i, num_norms)
        return np.power(result, 1 / num_norms)


def corss_entroy_loss(out_layer_list, num_classes):
    """
    交叉熵损失函数
    """
    N = len(out_layer_list)
    tmp = 0
    pass


def heye_loss(out_layer_list):
    N = len(out_layer_list)
    result = 0
    for i in out_layer_list:
        tmp = 1 - i
        result += max(0, tmp)
    return result / N

import matplotlib.pyplot as plt
x = range(-11, 20)
y = heye_loss(x)
print(y)