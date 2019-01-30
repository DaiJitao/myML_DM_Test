from gensim import corpora, models, similarities
import collections
from pprint import pprint  # pretty-printer 优美格式打印

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]


def combine(docs):
    """
    把整个文档合成一句话
    :param docs:
    :return:
    """
    result = ""
    for doc in docs:
        result += doc + " "
    return result.rstrip()  # 去除右边的空格


def remove_stop_words(stop_words, docs):
    for doc in docs:
        pass


stoplist = set('A for a of the and to in'.split())

print("停用词：", stoplist)
result = set()
for doc in documents:
    tmp = set(doc.split())
    result = result | tmp  # 并集运算
print("总词长度：" + str(len(result)), result)
result = result - stoplist
print("总词长度：" + str(len(result)), result)
comm_docs = combine(documents).split()

count = collections.Counter(comm_docs)
print(count)

# 去除整个语料库中仅仅出现一次的单词
one_time_words = set()
for key, freqs in count.items():
    if freqs == 1:
        one_time_words.add(key)
print("所有出现一次的单词：", one_time_words)


def sentences_removed_words(sentences, stop_words):
    words = sentences.strip().split()
    return [word for word in words if word not in stop_words]


def simpleWords_to_vec(docs, all_words):
    """
     仅仅把单词转换为向量
    :param docs:
    :param all_words:
    :return:
    """
    size = len(docs)
    vec_docs = [0] * size
    for i in range(size):
        doc = docs[i]  # 获取文档
        vec_doc = [0] * len(doc)
        for j in range(len(doc)):
            word = doc[j]  # 取出单词
            index = all_words.index(word)  # 找出该单词的下标
            vec_doc[j] = (index, 1.0)
        vec_docs[i] = vec_doc
    return vec_docs


def doc_to_vectors(docs, one_time_words, stop_words):
    stop_words = one_time_words | stop_words
    size = len(docs)
    new_docs = [0] * size
    all_words = []
    for i in range(size):
        sentence = docs[i]
        new_docs[i] = sentences_removed_words(sentence, stop_words)
        all_words = all_words + new_docs[i]

    # 获取整个语料库去除停用词和只出现一次单词后的总的单词数量
    all_words = list(set(all_words))
    return simpleWords_to_vec(new_docs, all_words)


mm = doc_to_vectors(documents, one_time_words, stoplist)
pprint(mm)
print("\n\n");
from gensim import models
tfidf = models.TfidfModel(mm)
for i in tfidf[ [[(10, 1.0), (11, 1.0)]] ]:
    print(i)
