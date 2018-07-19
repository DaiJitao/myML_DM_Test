import numpy as np
from common.obj2dict import list2dict

def calcShannonEnt(dataSet, class_index=-1):
    """
    计算信息熵: 默认按最后一列作为类别分类
    :param dataSet: [[1,1, 'A'],[2,2, "B"]] ; type:numpy.arrany
    :return:
    """
    (m, n) = dataSet.shape # m行， n列
    labels = dataSet[:,class_index] # 取出最后一列
    # 构建字典 key:label, v:次数
    _dict = list2dict(list(labels))
    _sum = 0
    for v in _dict.values():
        _sum += v
    probabilites = []
    for k in _dict.keys():
        tmp = _dict[k] / _sum
        probabilites.append(tmp)
    print("概率： ", probabilites)
    # 计算信息熵
    res = 0
    for i in probabilites:
        res += i * np.log2(i)
    return -res


if __name__ == "__main__":
    dd = np.array( [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']])
    res = calcShannonEnt(dd)
    print(res)
