#coding:utf-8

import tensorflow as tf

filter_weight = tf.get_variable('weights', [5,5,3,16],
                                initializer=tf.truncated_normal_initializer(stddev=0.1))
biases = tf.get_variable('biases', [16,],
                         initializer=tf.truncated_normal_initializer(stddev=0.1))
conv = tf.nn.conv2d(input, filter_weight, strides=[1,1,1,1], padding="SAME")
bias = tf.nn.bias_add(conv, biases)
actived_conv = tf.nn.relu(bias)

pool = tf.nn.max_pool(actived_conv, ksize=[1,3,3,1],
                      strides=[1,2,2,1]
                      ,padding='SAME')
