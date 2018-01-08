# _*_ coding:utf-8 _*_
# 使用python3.x解释器

import tensorflow as tf

a = tf.constant([1.0,2.0], name='a')
b = tf.constant([2.0,3.0], name='b')

print(a.graph)
print(tf.get_default_graph())

g = tf.Graph()
with g.device('/gpu:0'):
    result = a + b
    print(result)

w1 = tf.Variable(tf.random_normal([2,3], stddev=1)) # 2行3列 标准差为1 平均值为0