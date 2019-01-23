
from data_mining_demo.machine_learning_in_action.load_data import DataOp
import numpy as np

fileName = r"E:\pycharm_workspace\myML_DM_Test\resource\machineLearningInAction\Ch13\testSet.txt"

dataOp = DataOp(fileName)
data = dataOp.loadDateSet()
print(data)
meanVals = np.mean(data, axis=0)
print(meanVals)
res = data - meanVals
print("去除均值")
print(res)
covMat = np.cov(res, rowvar=0)
print("协方差矩阵")
print(covMat)
eiValus, vector = np.linalg.eig(covMat)
print("特征值")
print(eiValus)
print("特征向量")
print(vector)
print("提取特征向量")
tmp = np.mat(vector[:, -1])
print(tmp)
print(tmp.shape)
print("特征变化")
bian = res.dot(tmp.T) + meanVals
print(bian)
print(bian.shape)

def plot_():
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter()

