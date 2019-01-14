import numpy as np

def vetctor_norm(data):
    l = len(data)
    if l == 0:
        raise Exception("向量为空")
    else:
        return np.linalg.norm(c)


c = np.array([4/3, -1, 2/3])
c_len = vetctor_norm(c)
u = c / c_len #单位向量

A = np.array([[4, 8], [11, 7], [14, -2]])
print(A.shape)
print(A.T.shape)

M = A.dot(A.T)
print("M:")
print(M)
a, b = np.linalg.eig(M)
print("特征值", a)
print("特征向量\n", b)
print("取最大特征值", int(a[0]))
