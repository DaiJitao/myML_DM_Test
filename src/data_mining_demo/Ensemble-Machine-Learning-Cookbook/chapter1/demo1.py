import os
import numpy as np
import pandas as pd

os.chdir("../data/Ensemble-Machine-Learning-Cookbook/chapter01") # 修改路径
print(os.getcwd()) # 打印路径
house_price = pd.read_csv('HousePrices.csv')
print(house_price.head())
print(house_price.shape)
print(house_price.describe())
print(house_price.drop(['Id'], axis=1, inplace=True)) # 0 代表行；1代表列
print(house_price.shape)