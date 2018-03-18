# coding;utf-8

from sklearn.feature_extraction import DictVectorizer

onehot_encoder = DictVectorizer()
instances = [{'city': 'New York'}, {'city': 'San Francisco'}, {'city': 'Chapel Hill'}]
print(onehot_encoder.fit_transform(instances).toarray())

""" 文字特征提取 """
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(stop_words='english')
corpus = ['文字 特征 提取', 'Duke lost the basketball game',
          'I ate a sandwich'
          ]
print(len(corpus))
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)
# 计算欧氏距离
from sklearn.metrics.pairwise import euclidean_distances
counts = vectorizer.fit_transform(corpus).todense()
for x, y in [[0, 1],[0, 2],[1, 2]]:
    dist = euclidean_distances(counts[x], counts[y])
    print('文档{}与文档{}的距离{}'.format(x, y, dist))