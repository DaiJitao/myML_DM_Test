#!/usr/bin/env python
# coding: utf-8

# In[5]:


from keras.datasets import mnist # 导入数据集
from keras.datasets import imdb


# In[7]:


train, test =  imdb.load_data(num_words=10000) # mnist.load_data()


# In[9]:


print type(train)
print type(test)


# In[10]:


print len(train)


# In[11]:


train_data, train_labels = train
test_data, test_lables = test


# In[12]:


print train_data
print len(train_data)


# In[15]:


print train_data[0]
print len(train_data[0])
print len(train_data[1])


# In[16]:


from keras.datasets import reuters


# In[17]:


(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)


# In[18]:


len(train_data[10])


# In[19]:


# 构建网络
from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))


# In[20]:


model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])


# In[26]:


import numpy as np
def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results

def to_one_hot(labels, dimension=46):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label]
    return results


# In[25]:


x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)


# In[27]:


one_hot_train_labels = to_one_hot(train_labels)
one_hot_test_labels = to_one_hot(test_labels)

from keras.utils.np_utils import to_categorical
one_hot_train_labels = to_categorical(train_labels)
one_hot_test_labels = to_categorical(test_labels)


# In[28]:


x_val = x_train[:1000]
partial_x_train = x_train[1000:]
y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]


# In[29]:


# 开始训练网络， 20个轮次

history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val))


# In[31]:


get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


# In[ ]:




