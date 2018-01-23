# coding:utf-8

import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 加载数据集MNIST
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('E:\\data\\MNIST_data_sets\\', one_hot=True)

print(mnist.train.images.shape, mnist.train.labels.shape)
print(mnist.test.images.shape, mnist.test.labels.shape)
print(mnist.validation.images.shape, mnist.validation.labels.shape)

x = tf.placeholder("float", [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)  # 预测值

y_ = tf.placeholder("float", [None, 10])  # 新的占位符用于输入正确值,输入真实的label
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.005).minimize(cross_entropy)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # with tf.device("/gpu:1"):
    for i in range(100):
        # print(i)
        batch_xs, batch_ys = mnist.train.next_batch(1000)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        # print(sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys}))
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
    print("end")
