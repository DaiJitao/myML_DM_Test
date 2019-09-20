# 二分类问题

from keras.datasets import imdb

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

print(x_train)
print(type(x_train))
