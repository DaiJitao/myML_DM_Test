# coding:utf-8

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

file = "E:/data/MNIST_data_sets/"
mnsit = input_data.read_data_sets(file, one_hot=True)

X = tf.placeholder(tf.float32, [None, 784])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))


y = tf.nn.softmax(tf.matmul(X, W) + b) # 预测的概率分布

## 定义损害函数
y_ = tf.placeholder(tf.float32, [None, 10]) # 真实的概率分布
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
# 定义优化器
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
init = tf.global_variables_initializer()
n_iter = 1000
with tf.Session() as sess:
    sess.run(init)
    for i in n_iter:
        batch_xs, batch_ys = mnsit.train.next_batch(100)
        sess.run(train_step, feed_dict={X: batch_xs, y_: batch_ys})
        if i % 20 == 0:
            data = sess.run(loss, feed_dict={xs:x_data, ys:y_data})
            print(data)
            print(prediction)


