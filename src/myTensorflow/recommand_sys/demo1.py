import numpy as np
from common.load_data import LoadData
from common.my_oneHot import to_one_hot_code
""" 暂不考虑数据的标准化 """

file = r'D:\sys_recommand\republish_test.csv'
load_data = LoadData(file)
data = load_data.load_csv()

all_labels = data.service_type
# 为了在行上进行操作，引入ix
all_data = data.ix[:, 1:24]
"""转换为np数组"""
all_values = np.array(all_data.values)
encode = to_one_hot_code
all_labels = np.array([encode(x) for x in all_labels.values])

# 划分训练集、测试集和验证集
print(all_labels.shape)