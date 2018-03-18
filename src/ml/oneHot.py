#coding:utf-8

from sklearn import preprocessing
import numpy as np

data = np.array(
    [[3, -1.5, 2, -5.4],
     [0, 4, -0.3, 2.1],
     [1, 3.3,-1.9, -4.3]])

# 均值移除
print("Mean: ", np.mean(data))
data_std = preprocessing.scale(data)
print(data_std.mean())
print(data_std.mean(axis=0))

# 范围缩放
data_scaler = preprocessing.MinMaxScaler(feature_range=(1,2))
date_scaled = data_scaler.fit_transform(data)
print("scaled data = \n", date_scaled)

# 归一化处理
data_normalized = preprocessing.normalize(data, norm='l1') # L1范数
print(type(data_normalized))
print(data_normalized)
print(data_normalized[0])
sum_data = 0
for i in data_normalized[0]:
    if i < 0:
        i = i * (-1)
    sum_data = sum_data + i
print(sum_data)

print("=================")

encoder = preprocessing.OneHotEncoder()
encoder.fit([[0, 2, 1, 12], [1, 3, 5, 3], [2, 3, 2, 12], [1, 2, 4, 3]])
encoded_vector = encoder.transform([[2, 3, 5, 3]]).toarray()
print(encoded_vector)
print(len(encoded_vector[0]))