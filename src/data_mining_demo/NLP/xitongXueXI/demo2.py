import jieba
import jieba.posseg as psg
seg_list = jieba.cut('我在学习自然语言处理')
print("/".join(["{0}".format(i) for i in seg_list]))

seg_list = psg.cut('我在学习自然语言处理')
print(" ".join([ "{0}/{1}".format(i, t) for i, t in seg_list ]))