# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:31:27 2016

@author: Administrator
"""

import pandas as pd
import numpy as np

#读取数据
good=pd.read_csv("d:/data/good.csv",index_col=0)
bad=pd.read_csv("d:/data/bad.csv",index_col=0)

#使用现有情感分析工具SnowNLP，其中情感分析功能目前只针对商品评价进行判断
from snownlp import SnowNLP
gm=[]
#对好评中的每个评论进行情感分析
for com in good['comment']:
    gm.append(SnowNLP(com.decode('utf-8')).sentiments)
gm=np.array(gm)
#计算好评中的正面情感平均得分
gm.mean()
#打印出好评中正面情感概率少于0.4的评论
good['comment'][gm<0.4]
gm[gm<0.4]

bm=[]
#对差评中的每个评论进行情感分析
for com in bad['comment']:
    bm.append(SnowNLP(com.decode('utf-8')).sentiments)
bm=np.array(bm)
#计算差评中的正面情感平均得分
bm.mean()
#打印出差评中正面情感概率大于0.6的评论
bad[bm>0.6]
bm[bm>0.6]


#使用分类器
#使用结巴分词提取关键词作为特征
import jieba
import jieba.analyse
def key_words(com):
    keys=jieba.analyse.extract_tags(com,topK=5)
    i=1
    key_words={}
    for key in keys:
        key_words['key'+str(i)]=key
        i=i+1
    return key_words

#构造用于分类的特征向量
comment_set=([(comment, 'good') for comment in good['comment']] +
        [(comment, 'bad') for comment in bad['comment']])
featuresets = [(key_words(com), g) for (com,g) in comment_set]

#划分训练集与测试集
import random
random.shuffle(comment_set)
train_set, test_set = featuresets[400:], featuresets[:400]

#使用训练集训练贝叶斯分类器
import nltk
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)

#使用多个分类器进行比较
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def score(classifier):
    classifier = SklearnClassifier(classifier) #在nltk 中使用scikit-learn 的接口
    classifier.train(train_set) #训练分类器
    pred = classifier.classify_many([fea for (fea,tag) in test_set]) #对开发测试集的数据进行分类，给出预测的标签
    return accuracy_score([tag for (fea,tag) in test_set], pred) #对比分类预测结果和人工标注的正确结果，给出分类器准确度
    
print 'BernoulliNB`s accuracy is %f' %score(BernoulliNB())
print 'MultinomiaNB`s accuracy is %f' %score(MultinomialNB())
print 'LogisticRegression`s accuracy is %f' %score(LogisticRegression())
print 'SVC`s accuracy is %f' %score(SVC())
print 'LinearSVC`s accuracy is %f' %score(LinearSVC())
print 'NuSVC`s accuracy is %f' %score(NuSVC())    
        
#更改特征
#对所有评论进行分词        
comment_words=[]
for  com in good['comment']:
    seg_list = jieba.cut(com.decode('utf-8'), cut_all=False)
    for seg in list(seg_list):
        comment_words.append(seg)  
    
for  com in bad['comment']:
    seg_list = jieba.cut(com.decode('utf-8'), cut_all=False)
    for seg in list(seg_list):
        comment_words.append(seg)  
        
#获取所有分词    
all_words = set(comment_words)
len(comment_words) #共1498个词语

#以词语是否出现作为特征
def document_features(comment):
    words = set(jieba.cut(comment.decode('utf-8'), cut_all=False))
    features = {}
    for word in all_words:
        features['contains(%s)' % word] = (word in words)
    return features


featuresets = [(document_features(com), g) for (com,g) in comment_set]

#划分训练集与测试集
import random
random.shuffle(comment_set)
train_set, test_set = featuresets[400:], featuresets[:400]

#评估各类分类器效果
classifier = nltk.NaiveBayesClassifier.train(train_set)
print 'bayesian`s accuracy is %f' %nltk.classify.accuracy(classifier, test_set)
print 'decision tree`s accuracy is %f' %nltk.classify.accuracy(classifier, test_set)
#print classifier.pseudocode(depth=4)

print 'MultinomiaNB`s accuracy is %f' %score(MultinomialNB())
print 'LogisticRegression`s accuracy is %f' %score(LogisticRegression())
print 'SVC`s accuracy is %f' %score(SVC())
print 'LinearSVC`s accuracy is %f' %score(LinearSVC())
print 'NuSVC`s accuracy is %f' %score(NuSVC())    


