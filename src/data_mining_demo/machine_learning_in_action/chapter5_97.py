import numpy as np

file = r'E:\pycharm_workspace\myML_DM_Test\resource\machineLearningInAction\Ch05\testSet.txt'


def loadDataSet(file):
    dataMat = []
    labelMat = []
    with open(file) as opf:
        for line in opf.readlines():
            data = line.strip('\n').split("	")
            tmp = [float(data[0]), float(data[1])]
            dataMat.append(tmp)
            labelMat.append(int(data[2]))
    return dataMat, labelMat


def sigmoid(inX):
    """
    :param inX: list or () or arrar
    :return:
    """
    dataList = []
    for tmp in inX:
        value = 1 / (1 + np.exp(-tmp))
        dataList.append(value)
    return dataList


def gradAscent(dataMatIn, classLabels):
    """梯度下降算法"""
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    m, n = np.shape(dataMatrix)  # (100, 2)
    alpha = .001
    maxCycles = 500
    weights = np.ones((n, 1))
    for i in range(maxCycles):
        tmp = dataMatrix * weights #(100. 1)
        y = sigmoid(tmp)  # 矩阵相乘
        y = np.mat(y)
        # error = np.mat(y) - labelMat
        # weights = weights + alpha * dataMatrix.transpose() * error
    return tmp # weights


dataArr, labelMat = loadDataSet(file)
y = gradAscent(dataArr, labelMat)
print(np.mat(y).shape)

# print(np.array(dataMat).shape)
# print(dataMat)
# print(np.mat(label).transpose())
# dotT = np.array(dataMat) * np.mat([[1],[1]])
# print(dotT)
