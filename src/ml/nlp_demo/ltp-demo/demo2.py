from gensim import models
from pyltp import Segmentor


content = "我毕业于清华大学,我朋友的名字叫戴掵莉，我哥们的名字叫付先军；阿尔艾斯是我的村庄名字"
model_path = "E:/ltp3_4/cws.model"

segmentor = Segmentor()
segmentor.load(model_path)
words = " ".join(segmentor.segment(content))
print(words)
tfidf = models.TfidfModel(words)
print(tfidf)
