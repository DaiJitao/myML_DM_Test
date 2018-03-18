#coding:utf-8

import tensorflow.examples.tutorials.mnist as input_data
import tensorflow as tf

a = tf.constant([[1.0, 2.0], [1.0, 2.0], [1.0, 2.0]])
sess = tf.Session()
print(sess.run(tf.sigmoid(a)))

def add_layer(input, in_size, out_size, activation_function=None):
    """ add a player
    activation_function:激活函数
    """
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Weights_plus_bias = tf.matmul(input, Weights) + biases
    if activation_function is None:
        return Weights_plus_bias
    else:
        return activation_function(Weights_plus_bias)