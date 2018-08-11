# coding:utf-8

import jieba.analyse as an

# an.textrank()
# an.extract_tags()

import jieba.posseg as pseg
import jieba

# jieba.enable_parallel(4)

words = pseg.cut("我爱自然语言处理")

for word, flag in words:
    print(word, flag)