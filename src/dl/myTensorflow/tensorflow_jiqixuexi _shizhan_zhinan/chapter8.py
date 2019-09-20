import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

data_dir = 'temp'
mnist = read_data_sets(data_dir)
train_xdata = np.array([np.reshape(x, (28, 28)) for x in mnist.train.images])
test_xdata = np.array([np.reshape(x, (28, 28)) for x in mnist.test.images])
train_labels = mnist.train.labels
test_labels = mnist.test.labels

batch_size = 100
learning_rate = .005
evaluation_size = 500
image_width = train_xdata[0].shape[0]
image_height = train_xdata[0].shape[1]
target_size = max(train_labels) + 1
num_channels = 1
generations = 500
eval_every = 5
conv1_features = 25 # 25个输出特征，或者说25个过滤器
conv2_features = 50
full_connected_size1 = 100

x_input_shape = [batch_size, image_width, image_height, num_channels]
x_input = tf.placeholder(dtype=tf.float32, shape=x_input_shape)
y_target = tf.placeholder(dtype=tf.float32, shape=(batch_size))
eval_input_shape = [evaluation_size, image_width, image_height, num_channels]
eval_input = tf.placeholder(tf.float32, shape=eval_input_shape)
eval_target = tf.placeholder(tf.float32, shape=(evaluation_size))

# 说明卷积层的权重和偏置
conv1_weights = tf.Variable(initial_value=tf.truncated_normal(stddev=.1, dtype=tf.float32,
                                                              shape=[4, 4, num_channels, conv1_features]))
conv1_bias = tf.Variable(initial_value= tf.zeros([conv1_features]) , dtype=tf.float32)

conv2_weights = tf.Variable(initial_value=tf.truncated_normal(shape=[4, 4, conv1_features, conv2_features], stddev=.1, dtype=tf.float32))
conv2_bias = tf.Variable(initial_value= tf.zeros([conv2_features]) , dtype=tf.float32)

# 全连接层
resulting_width = ''
resulting_height = ''
full1_input_size = ''
full1_weight = ''
full1_bias = ''
full2_weight = ''
full2_bias = ''




def my_conv_net(input_data):
    conv1 = tf.nn.conv2d(input=input_data, filter=[image_width, image_height, 1, 25]
                              , strides=[1, 1, 1, 1])
    conv1_relu = tf.Relu(conv1_conv)
    conv1_pool = tf.nn.max_pool(conv1_relu, ksize=[], strides=[, , , 25], )
    conv2_conv = tf.nn.conv2d(input=train_xdata, filter=[image_width, image_height, 1, 25]
                              , strides=[1, 1, 1, 1])
    conv2_relu = tf.Relu(conv1_conv)
    conv2_pool = tf.nn.max_pool(conv1_relu, ksize=[], strides=[, , , 25], )

    # 全连接层1
    # 全连接层2
    return




