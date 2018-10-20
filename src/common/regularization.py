import numpy
import numpy as np


# 正则化技术
# 正则化技术
# L0 L1 L2 范数的计算方法


def get_L0(vector):
    cout = 0
    for i in vector:
        if i != 0:
            cout += 1
    return cout


def get_L1(vector):
    tmp = numpy.abs(vector)
    return numpy.sum(tmp)


def get_L2(vector):
    tmp = np.sum(np.square(vector))
    return numpy.sqrt(tmp)


data = [-1, 4]
print(get_L0(data))
print(get_L1(data))
print(get_L2(data))
