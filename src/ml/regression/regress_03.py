# coding;utf-8
"""
垃圾短信的分类
"""
import pandas as pd

# 读取数据
fileName = r"E:\pycharm_workspace\myML_DM_Test\src\ml\data_sets\spam\smsspamcollection\SMSSpamCollection.csv"

df = pd.read_csv(fileName, delimiter="\t", header=None)
print(df.head())
print()
print("spam" ,df[df[0] == 'spam'][0].count())
print('ham', df[df[0] == 'ham'][0].count())

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split

X_train_raw, X_test_row, Y_train_raw, Y_test_raw = train_test_split(df[1], df[0])
