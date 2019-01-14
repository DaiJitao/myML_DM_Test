from numpy import *

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

def KMeans(dataSet, centroids):
    pass


fileName = r"E:\pycharm_workspace\myML_DM_Test\resource\machineLearningInAction\Ch10\testSet.txt"
dataSet = loadDateSet(fileName)
print(dataSet[0])
print(dataSet)
dataSet = mat(dataSet)

print(randCent(dataSet, 6))


