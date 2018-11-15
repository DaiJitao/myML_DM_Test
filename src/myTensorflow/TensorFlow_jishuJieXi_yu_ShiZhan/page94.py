import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# 加载数据




with tf.Session() as sess:
    b = tf.nn.dropout(a, .5, noise_shape=[1,4])
    print sess.run(b)
    b = tf.nn.dropout(a, .5, noise_shape=[1,1])
    print sess.run(b)