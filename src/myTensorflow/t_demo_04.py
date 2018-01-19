#coding:utf-8

import tensorflow.examples.tutorials.mnist as input_data
import tensorflow as tf

a = tf.constant([[1.0, 2.0], [1.0, 2.0], [1.0, 2.0]])
sess = tf.Session()
print(sess.run(tf.sigmoid(a)))