

import pandas as pd
from pandas import DataFrame as df
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

dataFile = r'F:\pycharm_workspace\myML_DM_Test\resource\python_practice_Data_Analy_Min\chapter5\chapter5\demo\data\bankloan.xls'

data = pd.read_excel(dataFile)
df_data = df(data)
print(data)
print("DF: \n" ,df_data)

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

x = data.iloc[:,:8].as_matrix()
y = data.iloc[:, 8].as_matrix()
print("X \n", x)
print("Y \n", y)

rlr = RLR() #建立随机逻辑回归模型，筛选变量
rlr.fit(x, y) #训练模型



