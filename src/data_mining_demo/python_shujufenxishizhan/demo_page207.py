#coding:utf-8

""" 本实例源自《python_shujufenxishizhan》 """

from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体，仿宋体FangSong；微软雅黑：Microsoft YaHei
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是中文显示为方块的问题

iris = datasets.load_iris()
print("shape:", iris.data.shape)
print("data:")
print(iris.data[0:10,:])
print(iris.target, iris.target_names)
# x 表示长度， y表示宽度
x = iris.data[:, 0]
y = iris.data[:, 1]
species = iris.target

x_min, x_max = x.min(), x.max()
y_min, y_max = y.min(), y.max()

# plt.figure()
# plt.scatter(x, y, c=species)
# plt.xlabel("长度"); plt.ylabel("宽度")
# plt.xlim(x_min - 0.1 , x_max + 0.1) ; plt.ylim(y_min-0.1, y_max + 0.1)
# plt.xticks()
# plt.yticks()
# plt.show()
# 以上为探索数据
# 数据降维
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
del x
del y
x = iris.data[:, 1]
y = iris.data[:, 2]
x_reduced = PCA(n_components=3).fit_transform(iris.data)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x_reduced[:, 0], x_reduced[:, 1], x_reduced[:, 2], c=species)
ax.set_xlabel("第一主成分")
ax.set_ylabel("第二主成分")
ax.set_zlabel("第三主成分")
plt.show()


