# -*- coding: UTF-8 -*-

"""
朴素贝叶斯分类
"""


"""
函数说明:创建实验样本

Parameters:
    无
Returns:
    postingList - 实验样本切分的词条
    classVec - 类别标签向量
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-11
"""

def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # 切分的词条
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 类别标签向量，1代表侮辱性词汇，0代表不是
    return postingList, classVec

def createVocabList(dataSet):
    """ 转换为词汇列表 """
    returnvoSet = set([])
    for document in dataSet:
        returnvoSet = returnvoSet | set(document)
    return list(returnvoSet)

def document2Vec(vocabList, inputSet):
    """ 将文档向量化 """
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec

def trainNB0(trainMatrix,trainCategory):
    length = len(trainCategory)
    # c = list(set(trainCategory))
    count = 0
    for i in trainCategory:
        if i == 1:
            count += 1
    p_1 = count / float(length) # 先验概率
    p_0 = 1- p_1 # 先验概率








if __name__ == '__main__':
    postingList, classVec = loadDataSet()
    print('postingList:\n', postingList)
    myVocabList = createVocabList(postingList)
    print('myVocabList:\n', myVocabList)
    trainMat = []
    for postinDoc in postingList:
        trainMat.append(document2Vec(myVocabList, postinDoc))
    print('trainMat:\n', trainMat)
    print("词汇表长度", len(myVocabList))
    print("文档长度", len(postingList))
    print("向量化后的文档长度", len(trainMat))
    print("内部每一个文档长度", len(trainMat[0]))
    print("朴素贝叶斯分析---")

