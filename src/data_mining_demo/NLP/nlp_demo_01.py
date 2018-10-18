#coding:utf-8

import nltk
from nltk.text import TextCollection

data = "Hello world!"

tokens = nltk.word_tokenize(data)
print(tokens)
print("---------------------------------------")
corpus = TextCollection(['this is sentence one','this is sentence two','this is sentence three'])
print(corpus.tf_idf("this", "this is sentence four"))


import numpy as np
from numpy import dot

a = np.array([1,0])
p = np.array([[.9,.1], [.5, .5]])
n = dot(a ,p)
for i in range(1000):
    # n = dot(a,p)
    n = dot(n,p)



print("res::", n)

