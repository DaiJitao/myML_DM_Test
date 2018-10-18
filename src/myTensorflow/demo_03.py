
#coding:utf-8
import numpy as np

""" 交叉熵 衡量两个概率分布的距离"""

def cross_entropy(p, q):
    """
    p 为元组
    :param p: 正确的概率分布，实际值
    :param q: 预测的概率分布
    :return:
    """
    res = 0
    if len(p) != len(q):
        print("数据长度不一致")
        return "data error"
    for i in range(len(p)):
        p_x = p[i]
        q_x = q[i]
        res = res + p_x * np.log10(q_x)
    return -res

def soft_max(data, index):
    res = 0
    len_ = len(data)
    if len_ == 0 or index < 0:
        return 0
    # 先求分母
    temp = 0
    for i in data:
        temp += np.exp(i)
    return np.exp(data[index]) / temp


p = (1,0,0)
q1 = (.5,.4,.1)
q2 = (.8, .1, .1)

print("a ", cross_entropy(p, q1))
print("b ", cross_entropy(p, q2))

