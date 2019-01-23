import numpy as np

class DataOp(object):
    def __init__(self, fileName, delimitor = None):
        self.fileName = fileName
        self.delim = delimitor

    def loadDateSet(self):
        """ 加载数据 转为np.mat """
        mat_ = []
        fileName = self.fileName
        with open(fileName, "r") as file:
            for line in file.readlines():
                currentLine = line.strip().split()
                fltLine = list(map(float, currentLine))
                mat_.append(fltLine)
        return mat_