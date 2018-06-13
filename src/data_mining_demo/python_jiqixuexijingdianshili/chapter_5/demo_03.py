"""
寻找最近邻
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
# 创建一些示例的二维数据：
X = np.array([[1, 1], [1, 3], [2, 2], [2.5, 5], [3, 1],[4, 2], [2, 3.5], [3, 3], [3.5, 4]])
num_neighbors = 3
input_point = [2.6, 1.7]

plt.figure()
plt.scatter(X[:, 0], X[:, 1], marker='o', s = 25, color = 'k')
# plt.show()
knn = NearestNeighbors(n_neighbors=num_neighbors, algorithm='ball_tree').fit(X)
distances, indices = knn.kneighbors(input_point)

print("k nearest neighbors")
for rank, index in enumerate(indices[0][: num_neighbors]):
    print(str(rank + 1) + " -->", X[index])