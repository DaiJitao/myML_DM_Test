from gensim.models import FastText
import gensim

ldamodel = gensim.models.ldamodel.LdaModel

import fasttext as ff

train_data = "F:/NLP资料/fasttext/trainData/Data_train.txt"

classifier = ff.skipgram(train_data, 'model')
print(classifier.words)
