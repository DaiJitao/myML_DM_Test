from keras.datasets import imdb
import numpy as np

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
word_index = imdb.get_word_index()
d = dict([(str(index), word) for word, index in word_index.items()])


# 独热编码
def vectorize_sequences(sequences, dim=10000):
    results = np.zeros((len(sequences), dim))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results


def wordsToArticle():
    for i, sequence in enumerate(x_train):
        print(i, " ".join([d.get(str(index)) for index in sequence]))


x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train = np.array(train_labels).astype('float32')
y_test = np.array(test_labels).astype('float32')

from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu', ))
model.add(layers.Dense(1, activation='sigmoid'))

# 编译模型
from keras import optimizers, losses, metrics

# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer=optimizers.RMSprop(lr=.001),
              loss='binary_crossentropy',
              metrics=[metrics.binary_crossentropy])

# 留出验证集
x_val = x_train[:10000]
partial_x_train = x_train[10000:]  # 训练集
y_val = y_train[:10000]
partial_y_train = y_train[10000:]  # 训练集

# 训练
history = model.fit(partial_x_train, partial_y_train, batch_size=512, epochs=20, validation_data=(x_val, y_val))

print(history.history)
print(type(history.history))
