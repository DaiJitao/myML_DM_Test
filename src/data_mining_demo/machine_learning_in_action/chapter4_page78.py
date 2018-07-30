def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

def createVocabList(dataSet):
    """
    所有的文本转换为单词集合
    :param dataSet:
    :return:
    """
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWord2Vec(vocaList, inputSet):
    """
    单个文档转换为词向量
    :param vocaList:
    :param inputSet:
    :return:
    """
    returnVec = [0] *len(vocaList)
    for word in inputSet:
        if word in vocaList:
            returnVec[vocaList.index(word)] = 1
        else:
            print("单词%s不在集合中", word)
    return returnVec

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix) # 获取文档总数

if __name__ == "__main__":
    data, classD = loadDataSet()
    print(data)
    setD = createVocabList(data)
    print(setD)
    vec = setOfWord2Vec(setD, data[0])
    print(vec)