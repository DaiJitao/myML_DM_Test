from numpy import *
from collections import Counter


def loadDateSet(fileName):
    """ 加载数据"""
    mat_ = []
    with open(fileName, "r") as file:
        for line in file.readlines():
            currentLine = line.strip().split()
            fltLine = list(map(float, currentLine))
            mat_.append(fltLine)
    return mat_


def distanceEclud(vectorA, vectorB):
    vectorA, vectorB = array(vectorA), array(vectorB)
    tmp = pow(vectorA - vectorB, 2)
    sum_ = sum(tmp)
    return sqrt(sum_)


def randCent(dataSet, K):
    dataSet = mat(dataSet)
    """ 初始化质心 """
    # 所有的初始化为0
    # 获取样例的长度
    n = dataSet.shape[1]
    # 建立之心
    centroids = mat(zeros((K, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = list(map(float, max(dataSet[:, j]) - minJ))
        centroids[:, j] = minJ + rangeJ * random.rand(K, 1)
    return centroids

def getMeans(data):
    return np.mean(data, axis=0)

def init_Centroid_save(k):
    if k <= 0:
        return []
    d = dict()
    l = []
    for i in range(k):
        d.update({i: l})
    return d

def getMinDist(dict):
    """
    求字典中最小value的key
    :param dict:
    :return:
    """
    c = Counter(dict).most_common(-1) # 求出距离最近的质心（1， 12.3345）
    return c[0]

def isChangedCluster(data1, data2, k):
    """
    如果data1 与 data2 相等 则返回True
    :param data1:
    :param data2:
    :param k:
    :return:
    """
    for i in range(k):
        if data1[i] != data2[i]:
            return False
        else:
            return True


def KMeans(dataSet, centroids, distance, k, iterTimes=None, error=None):
    rows, cols = dataSet.shape
    centrids_size = len(centroids)
    isChangeCluster = True
    count = 0
    result = init_Centroid_save(k)  # 存储第t次
    result_plus_t = init_Centroid_save(k)  # 存储第t+1次
    while isChangeCluster:
        if iterTimes != None:
            count += 1
            if count > iterTimes:
                isChangeCluster = False
                break
        for row in range(rows):  # 计算每个点到质心的距离
            distances = dict()  # 存储距离{0: 12, 1:16}0为质心 12为距离
            vectorA = dataSet[row]
            for centroid in range(centrids_size):  # 遍历质心
                vectorB = dataSet[centroid]
                dist = distance(vectorA, vectorB)
                distances[centroid] = dist
            centroid_index = getMinDist(distances)
            result_plus_t[centroid_index].append(vectorA)  # 把vectorA 做标记
        # 判断第t次 和 t+1 次的点的分配是否还在变化，如果变化，继续迭代；否则，终止迭代
        isEqual = isChangedCluster(result, result_plus_t, k)
        if isEqual == False:
            for i in range(k):
                result[i] = result_plus_t[i]
                result_plus_t[i].clear()
        else:  # 标记已经分配完毕 停止迭代
            isChangegCluster = False
            break
        # 更新质心
        for i in range(k):
            centroids[i] = getMeans(result_plus_t[i])


fileName = r"E:\pycharm_workspace\myML_DM_Test\resource\machineLearningInAction\Ch10\testSet.txt"
dataSet = loadDateSet(fileName)
print(dataSet[0])
print(dataSet)
dataSet = mat(dataSet)

print("centorids;", randCent(dataSet, 6))




















