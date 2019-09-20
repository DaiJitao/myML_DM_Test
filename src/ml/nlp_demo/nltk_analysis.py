# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:31:27 2016

@author: Administrator
"""
# 划分训练集与测试集
import random
import re
import pandas as pd
from tools.utils import STOP_WORDS

# 使用分类器
# 使用结巴分词提取关键词作为特征
import jieba
import jieba.analyse

# 读取数据
good = pd.read_csv("../data/tanSongBo/hotel_pos.csv", index_col=0)
bad = pd.read_csv("../data/tanSongBo/hotel_neg.csv", index_col=0)
pattern = '[’!"#$%&\'()*+,-./:;<=>《》，。·“”（）、；：‘’？【】—！●■�0123456789．・９８７６５４３２１０／％［］×…?@[\\]^_`{|}~]+'


def words(text):
    cut_text = jieba.cut(text)
    result_words = []
    for word in cut_text:
        if word not in STOP_WORDS:
            result_words.append(word)
    return result_words


def key_words(com):
    ''' {'key1': '我要', 'key2': '伤心', 'key3': '爆炸', 'key4': '姐姐', 'key5': '变成', 'key6': '真的', 'key7': '可是'} '''
    com = re.sub(r'\s+', '', com)
    com = re.sub(r'\d+', '', com)
    com = re.sub(r'[a-zA-Z]{1,2}', '', com)
    keys = words(com)
    i = 1
    key_words = {}
    for key in keys:
        key_words['key' + str(i)] = key
        i = i + 1
    return key_words


# 构造用于分类的特征向量
comment_set = ([(comment, '1') for comment in good['text']] +
               [(comment, '-1') for comment in bad['text']])

featuresets = [(key_words(com), g) for (com, g) in comment_set]
print(len(featuresets))
data = []
for dict_v, lable in featuresets:
    v = " ".join(list(dict_v.values()))
    lable = "__label__" + lable
    data.append(lable + "  " + v)

data = data + data
random.shuffle(data)
pd.Series(data[2000:]).to_csv("../data/sentiment/enhancement/train_data.txt", index=False)
pd.Series(data[:2000]).to_csv("../data/sentiment/enhancement/test_data.txt", index=False)

train_set, test_set = featuresets[800:], featuresets[:800]
print()
# 使用训练集训练贝叶斯分类器
import nltk

# 使用训练集训练模型（核心就是求出各种后验概率）
classifier = nltk.NaiveBayesClassifier.train(train_set)
# 估计分类器的准确性
print("nltk 贝叶斯分类器的准确率：", nltk.classify.accuracy(classifier, test_set))
