
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
    return 1 / (1 + np.exp(-inX))

def gradAscent(dataMatIn, classLabels):
    """梯度下降算法"""
    dataMatrix = np.mat(dataMatIn)

dataMat, label = loadDataSet(file)

print(np.array(dataMat).shape)
