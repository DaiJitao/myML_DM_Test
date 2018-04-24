#coding:utf-8

import tensorflow.examples.tutorials.mnist as input_data
import tensorflow as tf

a = tf.constant([[1.0, 2.0], [1.0, 2.0], [1.0, 2.0]])
<<<<<<< HEAD
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
=======

state = tf.Variable(0, name="counter")
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)
init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(state))
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
>>>>>>> f94936d3224b36aa2eec75994eae8c0de95e7e37
