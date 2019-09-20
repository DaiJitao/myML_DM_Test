import tensorflow as tf
import numpy as np

x_vs = np.array([1., 3., 5., 7., 9.])
x_data = tf.placeholder(dtype=tf.float32)
m_const = tf.constant(3.)
my = tf.multiply(x_data, m_const)
sess = tf.Session()
for x_v in x_vs:
    d = sess.run(my, feed_dict={x_data: x_v})
    print(d)

sess.close()
