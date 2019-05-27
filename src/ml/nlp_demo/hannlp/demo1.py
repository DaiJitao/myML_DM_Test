from pyhanlp import *
import jieba

HanLP.Config.ShowTermNature = False

print(HanLP.segment("你好，欢迎在Python中调用HanLP的API"))
print(jieba.cut("你好，欢迎在Python中调用HanLP的API"))



