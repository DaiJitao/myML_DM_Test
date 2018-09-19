

import jieba

contxt = "CSDN博客结构之法算法之道的作者July"

seg_list = jieba.cut(contxt)
print("分词结果：" , " ".join(seg_list))