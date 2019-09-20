import sys
import os

""" 关键词提取 """

import os
import sys
import json
import re
import jieba_fast as jieba

pattern = re.compile(u'[^a-zA-Z\u4E00-\u9FA5]')  # 非英文字母和非汉字


# 加载停用词
def getStopWords(file=r'F:\pycharm_workspce\myML_DM_Test\src\NLP\word2vector\data\stopwords2.txt'):
    stopWords = set()
    with open(file, mode='r', encoding='utf-8') as data:
        for line in data.readlines():
            stopWords.add(line.strip())
    return stopWords


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    files = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\\%s' % (filepath, allDir))
        files.append(child)  # .decode('gbk')是解决中文显示乱码问题
    return files


def loda_data(filepath):
    docs = []
    linesnum = 100000
    count = 0
    stopWords = getStopWords()
    with open(filepath, encoding='utf-8', mode='r') as file:
        for i in range(100000):
            line = file.readline()
            dictData = json.loads(line)
            content = dictData['content'].strip()
            # title = dictData['title'].strip()
            # content = content + " " + title
            if len(content) != 0:
                doc = [word for word in jieba.cut(content) if
                       len(word) > 0 and word not in stopWords and len(pattern.findall(word)) == 0]
                if len(doc) != 0:
                    docs.append(doc)
    return docs


dataFilePath = r"F:\NLP_learnings\文本数据集\长文本情感分析数据"
dataFilePath = r'F:\pycharm_workspce\xinhua_project\waterArmyDetection\data\all_data_4.txt'

'''单词编码'''


def codeWords(docs):
    words = set()
    for doc in docs:
        for word in doc:
            words.add(word)
    index_word = [{index: word} for index, word in enumerate(words)]
    word_index = [{word: index} for index, word in enumerate(words)]
    return index_word, word_index


def TF_IDF(docs):
    pass


if __name__ == "__main__":
    docs = loda_data(dataFilePath)
    index_word, word_index = codeWords(docs)
    print(index_word)
