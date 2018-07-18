
from numpy import *
import operator
from common.sort import sort3 as sort_dict
from common.sort import sort1 as sort_dict_big2small

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
print("\n")
print(labels)

def distance(f1, f2):
    """
    :param data1: list
    :param data2: list
    :return:
    """
    data1 = list(f1)
    data2 = list(f2)
    n = len(data1)
    if n != len(data2):
        print("计算距离错误，数据有误")
        return None
    else:
        sum_ = 0
        for i in range(n):
            sum_ += (data1[i] - data2[i]) ** 2
        return sum_ ** 0.5
print(distance([4,2], [2,1]) ** 2)

def max_label(list_):
    dict_ = {}
    for i in list_:
        if i not in  dict_:
            dict_[i] = 1
        else:
            v = dict_[i]
            dict_[i] = v + 1
    print(dict_)
    data = sort_dict_big2small(dict_)
    return data[0][0] # dd = data[0]; return dd[0]

def classify(fdata, dataSet, labels, k=3):
    """
    :param fdata: 待预测数据
    :param dataSet:  数据样本
    :param labels:  标签
    :param k:
    :return:
    """
    (m, n) = dataSet.shape
    # 首先检查数据是否符合规范
    if m != len(labels):
        print("数据有误")
        return
    if n != len(fdata):
        print("数据有误")
        return
    else:
        distance_dict = {}
        for i in range(m): # 遍历dataSet
            distance_ = distance(fdata, dataSet[i])
            distance_dict[str(i)] = distance_
        print("距离 类别")
        print(distance_dict)
        class_dict = sort_dict(distance_dict)
        predict_list = []
        for item in class_dict:
            label = labels[int(item[1])]
            print(item[0], label)
            predict_list.append(label)
        return max_label(predict_list[:k])

pp = classify([0, 0], dataSet=group, labels=labels, k=3)
print("pp-->", pp)









