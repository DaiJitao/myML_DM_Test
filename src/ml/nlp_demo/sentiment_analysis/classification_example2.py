# coding:utf-8
import fasttext as ft
import path

# First download the dbpedia.train using https://github.com/facebookresearch/fastText/blob/master/classification-example.sh
# on test/ and move to the example directory

output = '../../models/sentiment-classifier'
input_file = '../../data/sentiment/train_data.txt'
test_file = '../../data/sentiment/test_data.txt'

# set params
dim = 300  # 10->100_200
lr = 0.01
epoch = 10
min_count = 1
word_ngrams = 4  # 3->4
bucket = 20000
thread = 4
silent = 1
label_prefix = '__label__'
# Train the classifier
classifier = ft.supervised(input_file, output, dim=dim, lr=lr, epoch=epoch,
                           min_count=min_count, word_ngrams=word_ngrams, bucket=bucket,
                           thread=thread, silent=silent, label_prefix=label_prefix)

# Test the classifier
result = classifier.test(test_file)
print
'准确率:', result.precision
print
'召回率:', result.recall
print('Number of examples:', result.nexamples)

# Predict some text
# (Example text is from dbpedia.train)
texts = ['酒店 服务 态度 很差 不 熟练 有待 加强']
labels = classifier.predict(texts)
print(labels)
