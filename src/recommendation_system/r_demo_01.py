#conding:utf-8

"""
python机器学习经典实例 Page92 推荐系统
"""

import numpy as np
from functools import reduce

def add3(input_array):
    return map(lambda x: x + 3, input_array)

def mul2(input_data):
    return map(lambda x : x*2, input_data)

def sub5(input_array):
    return map(lambda x : x-5, input_array)

def function_composer(*args):
    return reduce(lambda f, g: lambda x: f(g(x)), args)

if __name__=='__main__':
    arr = np.array([2, 5, 4, 7])
    arr1 = add3(arr)
    arr2 = mul2(arr1)
    arr3 = sub5(arr2)
    print("Output using the lengthy way:", arr3)
