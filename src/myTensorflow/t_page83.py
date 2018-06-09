# coding:utf-8

import tensorflow as tf

a = tf.constant([[-1., 2., 3., 4.]])
with tf.Session() as sess:
    b = tf.nn.dropout(a, 0.5, noise_shape=[1, 4])
    print(sess.run(b))
    b = tf.nn.dropout(a, .5, noise_shape=[1,1])
    print(sess.run(b))

x = 2
y = 3

op1 = tf.add(x, y)
op2 = tf.multiply(x, y)
with tf.Session() as sess:
    d = sess.run(op2)
    print(d)
    sess.close()