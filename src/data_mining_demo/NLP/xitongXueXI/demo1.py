#coding:utf-8
import jieba

seg_list = jieba.cut('我在学习自然语言处理', cut_all=True)

print(seg_list)

print("FULL Mode::", '/'.join(seg_list))

seg_list = jieba.cut("我在学习自然语言处理", cut_all=False)
print(seg_list)
print("Default Mode::", '/'.join(seg_list))


import jieba.analyse as analysis
file = r'E:\pycharm_workspace\myML_DM_Test\src\data_mining_demo\NLP\xitongXueXI\data.txt'
lines = open(file, 'r', encoding='UTF-8').read()
print(lines)

tags = analysis.extract_tags(lines, topK=30, withFlag=True, allowPOS=())
print(type(tags))













