from common.load_data import LoadData
from pyltp import Segmentor
import jieba

model_path = "E:/ltp3_4/cws.model"
content = "我毕业于清华大学,我朋友的名字叫戴掵莉，我哥们的名字叫付先军；阿尔艾斯是我的村庄名字"

seg = Segmentor()
seg.load(model_path) # 加载语言模型 用于分词
words = seg.segment(content)
seg_words = " ".join(words)
print("LTP: ", " /".join(words))
jiebaWords = jieba.cut(content, HMM=True)
print("jieba: ", " /".join(jiebaWords))
print(seg_words)

# 词性标注
from pyltp import Postagger

pos = Postagger()
model_path = "E:/ltp3_4/pos.model"

pos.load(model_path) # 导入词性标注模型
pos_words = pos.postag(seg_words.split(" "))
for word, pt in zip(seg_words.split(" "), pos_words):
    print(word + "/" + pt)

""" 
从分词结果上来看，对于新词的识别ltp分词方法远高于结巴分词
"""
print()
print()
text = r"E:\pycharm_workspace\myML_DM_Test\resource\nlp_Data\C000008\10.txt"
GetData = LoadData()
content = None or GetData.load_txt(text)
words = seg.segment(content)
word2s = jieba.cut(content)
print(" /".join(words))
print(" /".join(word2s))

print("===============================================================")
from pyltp import NamedEntityRecognizer
# 命名实体识别
ner_path = "E:/ltp3_4/ner.model"
ner = NamedEntityRecognizer()
ner.load(ner_path)
content = " ".join(words)
pos_words = pos.postag(content.split(" "))
net_tags = ner.recognize(content.split(" "), pos_words)
print(net_tags)
result = ""
for word, pos, name in zip(content.split(" "), pos_words, net_tags):
    result += (word+"/"+pos+"/"+name+"   ")
print(result)
