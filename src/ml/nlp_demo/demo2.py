from matplotlib import pyplot as plt
# 可视化

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

fig = plt.figure()
plt.text(0.66, 0.41, "戴")

plt.show()

import re

data = "如果放到POST中将出错"

import jieba
jieba.suggest_freq(("中", "将"), True)
seg_list = jieba.cut(data,  HMM=False)

seg_list1 = jieba.cut_for_search(data)
print("Full mode:", "/ ".join(seg_list))
print("Full mode:", "/ ".join(seg_list1))
result = jieba.tokenize(data)
print(result)
for i in result:
    print(i)