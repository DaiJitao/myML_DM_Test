
import jieba


print(jieba.cut("车皮也很薄"))

for i in jieba.cut("车皮也很薄"):
    print(i)