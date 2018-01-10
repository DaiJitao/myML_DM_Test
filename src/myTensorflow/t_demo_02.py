# _*_ coding:utf-8 _*_

import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2,3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3,1], stddev=1, seed=1))
# 定义输入特征向量
x = tf.placeholder(dtype=tf.float32, shape=(3,2), name="input")
a_02 = tf.matmul(x, w1)
y = tf.matmul(a_02, w2)

with tf.Session() as sess:
    init_op = tf.initialize_all_variables()
    print(sess.run(init_op))
    print(sess.run(y, feed_dict={x:[[0.7,0.9],[0.1,0.4],[0.5,0.8]]}))

#定义损失函数
cross_entropy = 1