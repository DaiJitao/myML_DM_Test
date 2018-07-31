

import numpy as np
from common.figure_style import Figure_Style
from sklearn.cluster import KMeans
from sklearn import metrics as mt
from matplotlib import pyplot as plt
from common.utilities import  load_data

data_file = r'E:\pycharm_workspace\myML_DM_Test\resource\python_ml_instances\Chapter04\data_multivar.txt'
data = load_data(data_file)

def explore_data(data_file = None):
    # data_file = r'E:\pycharm_workspace\myML_DM_Test\resource\python_ml_instances\Chapter04\data_multivar.txt'
    # data = load_data(data_file)
    print("======")
    print(data)
    print(type(data))
    x = data[:, 0]
    y = data[:, 1]
    xmin, xmax = np.min(x), np.max(x)
    ymin, ymax = np.min(y), np.max(y)

    Figure_Style(1)
    fig = plt.figure()
    plt.scatter(x, y, marker='o', edgecolors='k')

    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.xticks()
    plt.yticks()
    plt.grid()
    plt.show()
    return data

num_clusters = 4
kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)
kmeans.fit(data)
# 设置网格数据的步长
step_size = 0.01
# 画出边界
x_min, x_max = min(data[:, 0]) - 1, max(data[:, 0]) + 1
y_min, y_max = min(data[:, 1]) - 1, max(data[:, 1]) + 1
x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))
# 预测网格中所有数据点的标记
predicted_labels = kmeans.predict(np.c_[x_values.ravel(), y_values.ravel()])

# 画出结果
predicted_labels = predicted_labels.reshape(x_values.shape)
plt.figure()
plt.clf()
plt.imshow(predicted_labels, interpolation='nearest',extent=(x_values.min(), x_values.max(), y_values.min(), y_values.max()),
           cmap=plt.cm.Paired, aspect='auto', origin='lower')
plt.scatter(data[:,0], data[:,1], marker='o',facecolors='none', edgecolors='k', s=30)

centroids = kmeans.cluster_centers_
plt.scatter(centroids[:,0], centroids[:,1], marker='o', s=200, linewidths=3, color='k', zorder=10, facecolors='black')

plt.title('Centoids and boundaries obtained using KMeans')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()






