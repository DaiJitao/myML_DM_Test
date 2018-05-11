#coding:utf-8
import numpy as np
""" demo """

"""
题目      对于长度为N的数组A，求连续子数组的和最接近0的值。
如数组A：1，-2, 3, 10，-4, 7, 2，-5 
它是所有子数组中，和最接近0的是哪个？
解题思路：
    设 sum(i) = sum(A[0:i]),  k=j - i,
     则有： 
    
"""
a = [1, -2, 3, 10, -4, 7, 2, -5]

def sum_demo(a):
    """
    求数组a的前i项和
    :param a: 列表
    :return:  列表
    """
    _sum = list()
    n = len(a)
    for i in range(n):
        _sum.append(np.sum(a[0:(i+1)]))
    return _sum

def solution(a):
    _sum = np.sort(sum_demo(a))
    return _sum
print(solution(a))





