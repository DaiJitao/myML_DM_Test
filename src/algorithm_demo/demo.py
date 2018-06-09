#coding:utf-8


from sympy import *
# 引入积分变量
from sympy.abc import s

def x(t):
    """
    t: V(t)
     """
    return log(t) - log(t-1)

def get_definite_integral(t):
    """
    求解定积分
    :param t: 输入值
    :return:
    """
    # 积分函数
    fs = x(s) / (t - s)
    temp = integrate(fs, (s, -float('inf'), float('inf')))
    return temp

def theta(t):
    # 反三角函数
    return atan(get_contraction_structure(t) / x(t))

def a_u(t):
    """
    求解单个u(t)
    :param t:
    :return:
    """
    return E ** (I * theta(t))

def get_all_u(t, N):
    if N > 0:
        for i in range(N):
            # 输入N次t
            pass
        return sum/N
    else:
        return None

