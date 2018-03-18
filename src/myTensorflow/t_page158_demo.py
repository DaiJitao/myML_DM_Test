#coding:utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(0,2,300)[:, np.newaxis]

noise = np.random.normal(0, 0.05, x_data.shape)

y_data = np.sqrt(x_data) - 0.5 + noise
# plt.plot(x_data, y_data)
# plt.show()

xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

h1 = add_layer(xs, 1, 20, activation_function=tf.nn.relu)
prediction = add_layer(h1, 20, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
mydata = []
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(10000):  # 训练1000 次
        sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
        if i % 500 == 0:  # 􂆣 50 次􁠧印出一次􁤳􀼅􀘐
            data = sess.run(loss, feed_dict = {xs: x_data, ys: y_data})
            mydata.append(data)
            print(data)

plt.plot(mydata)
plt.show()

