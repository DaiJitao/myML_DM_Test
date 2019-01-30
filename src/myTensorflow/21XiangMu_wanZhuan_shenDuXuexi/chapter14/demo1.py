import zipfile
from collections import Counter
import time
from pprint import pprint
import redis
import os
import pickle

conn = redis.Redis()
text8 = r"E:\data\nlp_data\text8"
key = "words"

def read_date(file_name, key = "words"):
    if None == conn.get(key):
        with open(file_name, "r") as f:
            content = f.read()
            conn.set(key, content)
    else:
        data = conn.get(key)  # data 为字节类型
        data = str(data, encoding='utf8')  # 字节转换为字符串
        words = data.split()
        return words


words = read_date(text8)
print(words[:20])

count = [("UNK", -1)]
count.extend(Counter(words[:50]).most_common(10))
print(count)
va = dict()
for word, _ in count:
    print(word, len(va))
    va[word] = len(va)
print(va)

dataFile = "./data.txt"
def build_dataSet(words, all_words_size):
    """
    建立一个只有50000词的词表
    :param words:
    :param all_words_size:
    :return:
    """
    count = [('UNK', 0)]
    tmp = Counter(words).most_common(all_words_size-1)
    count.extend(tmp)
    vocabulary = dict()
    for word, nums in count:
        vocabulary[word] = len(vocabulary)
    data = list()
    # 遍历所有语料库中的单词，如果单词在vocabulary中，转换其为nums;如果不在，转换其为UNK,再取nums
    for word in words:
        if word in vocabulary:
            index = vocabulary.get(word)
        else:
            index = vocabulary.get("UNK")
        data.append(index)
    return data


data = build_dataSet(words, 50000)

with open(dataFile, "wb" ) as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


print(data[:100])
print(Counter(data).most_common(100))
# print(data[:12])
# print(len(data))

#
# print(Counter(data[:100]).most_common())