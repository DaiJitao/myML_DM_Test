# from progressbar import *
# total = 1000
# def dosomework():
#     time.sleep(0.01)
# pbar = ProgressBar().start()
# for i in range(1000):
#     pbar.update(int((i / (total - 1)) * 100))
#     dosomework()


import numpy as np

s1 = "I like deep learning"
s2 = "I like NLP"
s3 = "I enjoy flying"

sentences = [s1, s2, s3]


def get_words(sentences):
    data = set()
    for line in sentences:
        tmp = set(line.strip().split())
        data = data | tmp
    return list(data)

print(get_words(sentences))



# 编造文本、分词
from jieba import lcut
sentences = ['我吴彦祖', '我张学友', '吴彦祖我', '张学友我刘德华吴彦祖',
             '酸奶芝士', '芝士酸奶', '芝士蛋糕', '酸奶芝士蛋糕']
ls_of_words = [lcut(sentence) for sentence in sentences]

# 生成字典和词ID
from gensim.corpora import Dictionary
dt = Dictionary(ls_of_words).token2id
ls_of_wids = [[dt[word] for word in words] for words in ls_of_words]

# 共现矩阵
import numpy as np
dimension = len(dt)  # 维数
matrix = np.matrix([[0] * dimension] * dimension)
def co_occurrence_matrix(ls):
    length = len(ls)
    for i in range(length):
        for j in range(length):
            if i != j:
                matrix[[ls[i]], [ls[j]]] += 1
for ls in ls_of_wids:
    co_occurrence_matrix(ls)
print(matrix)

# 奇异值分解（Singular Value Decomposition）
U, s, Vh = np.linalg.svd(matrix, full_matrices=False)

# 聚类
X = -U[:, 0:2]
from sklearn.cluster import KMeans
labels = KMeans(n_clusters=2).fit(X).labels_
colors = ('y', 'g')

# 可视化
import matplotlib.pyplot as mp
mp.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
for word in dt.keys():
    i = dt[word]
    mp.scatter(X[i, 1], X[i, 0], c=colors[labels[i]], s=400, alpha=0.4)
    mp.text(X[i, 1], X[i, 0], word, ha='center', va='center')
mp.show()


