#coding:utf-8

import nltk
from nltk.text import TextCollection

data = "Hello world!"

tokens = nltk.word_tokenize(data)
print(tokens)
print("---------------------------------------")
corpus = TextCollection(['this is sentence one','this is sentence two','this is sentence three'])
print(corpus.tf_idf("this", "this is sentence four"))

