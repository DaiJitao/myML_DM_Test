import tensorflow as tf
from sklearn import datasets

iris = datasets.load_iris()
print(iris.data)
# 出生体重数据
import requests
url = 'https://www.umass.edu/statdata/data/lowbwt.dat'
file = requests.get(url)
print(file)
# 波士顿房价数据
# E:\pycharm_workspace\myML_DM_Test\resource\tensorflow_JiQiXueXi_ShiZhanZhiNan\chapter2\housing.data.txt
url2 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
data2 = requests.get(url=url2)
print("data2: {0}".format(data2))
for i in dir(data2):
    print(i)

# MNIST 数据
file = r'E:\pycharm_workspace\myML_DM_Test\resource\tensorflowData\MNIST_data_sets'
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets(file, one_hot=True)
print(len(mnist.train.images))

# 垃圾短信文本数据
import io
from zipfile import ZipFile
url3 = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'
r = requests.get(url3)
z = ZipFile(io.BytesIO(r.content))
