import numpy as np
from numpy import abs

x = np.array([1, 2]) # 列向量
y = np.array([3, 4])

print(x.dot(y.T))
data = np.mat([[1, 2], [3, 4]])

# 求矩阵的行列式
print(data)
d = np.linalg.det(data)
print(d)
# 求矩阵的逆
print(np.linalg.inv(data))
print(np.linalg.matrix_rank(data))

# 切比雪夫距离

def get_distance(x, y):
    size = len(x)
    result = []
    max_ = 0
    for i in range(size):
        if abs(x[i] - y[i]) > max_:
            max_ = abs(x[i] - y[i])
        return max_
print("d:", get_distance([1, 2, 3], [4, 5, 7]))