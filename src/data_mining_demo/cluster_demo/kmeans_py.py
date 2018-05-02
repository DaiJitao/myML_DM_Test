import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans

"""
k均值聚类的用法
python机器学习经典实例 Page68
"""
# 加载数据
data_path = "E:\\pycharm_workspace\\myML_DM_Test\\resource\\python_ml_instances\\Chapter01\\data_multivar.txt";
data = pd.read_table(data_path, header=None, delimiter=",")
# header=None:没有每列的column name，可以自己设定
# encoding='gb2312':其他编码中文显示错误
# delim_whitespace=True:用空格来分隔每行的数据
# index_col=0:设置第1列数据作为index

print(data[0])
# mydata = DataFrame(data, columns=["first", "second", "third", "three"])
# print(mydata)
plt.figure()

plt.scatter(data[0], data[1])
plt.title("Input data")
x_min, x_max = min(data[0]) - 1, max(data[0]) + 1
y_min, y_max = min(data[1]) - 1, max(data[1]) + 1
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()

num_clusters = 4
kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)
kmeans.fit(data)

step_size = .01
x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))
predicted_labels = kmeans.predict(np.c_[x_values.ravel(), y_values.ravel()])