# coding;utf-8

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
X0 = np.array([7, 5, 7, 3, 4, 1, 0, 2, 8, 6, 5, 3])
X1 = np.array([5, 7, 7, 3, 6, 4, 0, 2, 7, 8, 5, 7])

plt.figure()
plt.axis([-1, 9, -1, 9])
plt.grid()
plt.plot(X0, X1, 'k.')
plt.show()

print(len(X1))

def color_cluster(dataindex, dataSet, plt, k=4):
    index = 0


def loadDataSet(fileName, delimiter="\t"):
    """ https://blog.csdn.net/taoyanqi8932/article/details/53727841
        加载数据集
    """
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(delimiter)
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    from math import sqrt, pow
    data = sum(pow(vecA - vecB, 2))
    return sqrt(data)