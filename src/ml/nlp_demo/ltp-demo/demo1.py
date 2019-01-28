
from pyltp import Segmentor

model_path = "E:/ltp3_4/cws.model"
content = "我毕业于清华大学"

seg = Segmentor()
seg.load(model_path) # 加载语言模型 用于分词
words = seg.segment(content)
seg_words = " ".join(words)
print(" ".join(words))
print(seg_words)

# 词性标注
from pyltp import Postagger

pos = Postagger()
model_path = "E:/ltp3_4/pos.model"

pos.load(model_path) # 导入词性标注模型
pos_words = pos.postag(seg_words.split(" "))
for word, pt in zip(seg_words.split(" "), pos_words):
    print(word + "/" + pt)

