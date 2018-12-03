import tensorflow as tf


hello = tf.constant('hhh')
a = tf.constant([[12, 12], [1, 5]])
b = tf.constant([[1], [2]])
c = tf.matmul(a, b)

with tf.device("/cpu:0"):
    sess = tf.Session()
    print(sess.run(hello))
    print(sess.run(c))
    sess.close()
with tf.device("/cpu:1"):
    sess = tf.Session()
    print(sess.run(hello))
    print(sess.run(c))
    sess.close()