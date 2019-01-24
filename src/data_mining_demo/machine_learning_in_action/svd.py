import numpy as np
import numpy.linalg as la

data = np.array([[1, 1],
              [7, 7]])

U, Sigma, VT = np.linalg.svd(data)
print(U)
print("Sigma")
print(Sigma)
print("VT")
print(VT)


def loadExData():
    return [[0, 0, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [5, 5, 5, 0, 0],
            [1, 1, 1, 0, 0]]


def loadExData2():
    return [[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
            [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
            [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
            [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
            [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
            [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
            [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
            [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]

print("==================================")
data = loadExData()
U, Sigma, VT = np.linalg.svd(data)
print("U")
print(U)
print("Sigma")
print(Sigma)
print("VT")
print(VT)
Sig3 = np.mat([
               [Sigma[0], 0, 0],
               [0, Sigma[1], 0],
               [0, 0, Sigma[0]]
               ])
# 取矩阵U的前3列
tmp = U[:, :3] * Sig3 * VT[:3, :]
print("tmp")
print(tmp)
print("tmp")
for i in tmp:
    print(i)


def ecludSim(intA, intB):
    return 1.0 / (1.0 + la.norm(intA - intB))

def pearsSim(intA, intB):
    if len(intA) < 0:
        return 1.
    else:
        return .5 + .5 * np.corrcoef(intA, intB, rowvar=0)

def cosSin(intA, intB):
    num = np.float(np.dot(intA.T, intB))
    denom = la.norm(intB) * la.norm(intA)
    return .5 + .5 * (num / denom)
myMat = np.array(loadExData())

print("欧氏距离：")

print(myMat[:, 1])
print(myMat[:, 2])
print(ecludSim(myMat[:, 0], myMat[:, 0]))
print(pearsSim(myMat[:, 0], myMat[:, 2]))
import matplotlib.pyplot as plt
def demo_sim(data):
    result_eclu = []
    result_pears = []
    result_cos = []
    rows, cols = data.shape
    print("列", cols)
    for i in range(cols-1):
        t1 = data[:, i]
        t2 = data[:, i+1]
        result_eclu.append(ecludSim(t1, t2))
        result_pears.append(pearsSim(t1, t2))
        result_cos.append(cosSin(t1, t2))
    size = range(cols-1)
    plt.plot(size , result_eclu, label = "Eclud")
    plt.plot(size, result_cos, label = "cos")
    # plt.plot(size, result_pears, label = "Pears")
    plt.legend()
    plt.grid(True)
    plt.show()


myMat2 = np.array(loadExData2())
