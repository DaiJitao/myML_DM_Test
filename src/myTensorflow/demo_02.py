
import collections
import math
import os
import time
import random
import zipfile
import numpy as np
import urllib
import tensorflow as tf

words = "the quick brown fox jumped over the lazy dog"

url = 'http://mattmahoney.net/dc/'

def maybe_download(filename, expected_bytes):
    print("os.path: \n")
    print(os.path)
    if not os.path.exists(filename):
        filename, _ = urllib.request.urlretrieve(url + filename, filename)
    statinfo = os.stat(filename)
    if statinfo.st_size == expected_bytes:
        print('Found and verified', filename)
    else:
        print(statinfo.st_size)
        raise Exception('Failed to verify' + filename + '. Can you get to it with a browser?')
    return filename
filename = maybe_download('text8.zip', 31344016)
print("fileName");print(filename)

def read_data(filename):
    with zipfile.ZipFile(filename) as f:
        print("f.namelist ", f.namelist()) # f.namelist zip文件中的列表，
        data = tf.compat.as_str(f.read(f.namelist()[0])).split() # 以空格分
    return data

words = read_data(filename)
print("data Szie", len(words))


vocabulary_size = 50000

def build_dataSet(words):
    count = [['UNK', -1]]
    count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
    dictionary = dict()
    print("Count ", count)
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0
            unk_count = unk_count + 1
        data.append(index)
    count[0][1] = unk_count
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reverse_dictionary

data, count, dictionary, reverse_dictonary = build_dataSet(words)
print("data ", data[1])
del words # 清理内存
print("Most common words (+UNK)", count[:5])
print("Sample data", data[:10], [reverse_dictonary[i] for i in data[:10]])

