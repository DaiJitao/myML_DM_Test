#coding:utf-8
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cosine


n = 100
x1 = np.random.random_integers(0, 10, (n, 1))
x2 = np.random.random_integers(0, 10, (n, 1))
x3 = np.random.random_integers(0, 10, (n, 1))

p12 = 1 - pearsonr(x1, x2)[0][0]
p13 = 1 - pearsonr(x1, x3)[0][0]
p23 = 1 - pearsonr(x2, x3)[0][0]

d12 = (euclidean(x1, x2) / (2 *n))
d13 = (euclidean(x1, x3) / (2 *n))
d23 = (euclidean(x2, x3) / (2 *n))

c12 = cosine(x1, x2)
c13 = cosine(x1, x3)
c23 = cosine(x2, x3)

print("\n原始数据，没有标准化\n")
print("               x1_x2  x1_x3  x2_x3")
print('pearson       ', np.round(p12, decimals=4), np.round(p13, decimals=4),
      np.round(p23, decimals=4))
print('cos           ', np.round(c12, decimals=4), np.round(c13, decimals=4),
      np.round(c23, decimals=4))
print('euclidean  sq ', np.round(d12, decimals=4), np.round(d13, decimals=4),
      np.round(d23, decimals=4))

# 建立标准化器
stdz = StandardScaler()
x1_n = stdz.fit_transform(x1)
x2_n = stdz.fit_transform(x2)
x3_n = stdz.fit_transform(x3)

p12 = 1 - pearsonr(x1_n, x2_n)[0][0]
p13 = 1 - pearsonr(x1_n, x3_n)[0][0]
p23 = 1 - pearsonr(x2_n, x3_n)[0][0]

d12 = (euclidean(x1_n, x2_n) / (2 *n))
d13 = (euclidean(x1_n, x3_n) / (2 *n))
d23 = (euclidean(x2_n, x3_n) / (2 *n))

c12 = cosine(x1_n, x2_n)
c13 = cosine(x1_n, x3_n)
c23 = cosine(x2_n, x3_n)
print("\n标准化")
print("               x1_x2  x1_x3  x2_x3")
print('pearson       ', np.round(p12, decimals=4), np.round(p13, decimals=4),
      np.round(p23, decimals=4))
print('cos           ', np.round(c12, decimals=4), np.round(c13, decimals=4),
      np.round(c23, decimals=4))
print('euclidean  sq ', np.round(d12, decimals=4), np.round(d13, decimals=4),
      np.round(d23, decimals=4))