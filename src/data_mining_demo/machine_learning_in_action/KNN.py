
from numpy import *
import operator

def createDateSet():
    """
    建立数据集
    :return:
    """
    group = array([[1,1.1],[1,1],[0,0],[0,.1]],dtype=float16)
    labels = ['A', 'A', 'B', "B"]
    return group, labels

group, labels = createDateSet()
print(group.shape)
print("\n\n")
print(labels)