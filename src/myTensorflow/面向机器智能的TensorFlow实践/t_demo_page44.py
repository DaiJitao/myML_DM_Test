#coding:utf-8

import tensorflow as tf

a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_b")

c= tf.multiply(a,b, name="mul_c")
d = tf.add(a, b, name="add_d")

e = tf.add(a, d, name="add_e")

with tf.Session() as sess:
    tt = sess.run(e)
    print("tt", tt)