import tensorflow as tf
#加载数据集MNIST
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('E:\\data\\MNIST_data_sets\\', one_hot=True)


filter_weight = tf.get_variable(name='weight',
                                shape=[5, 5, 3, 16],
                                initializer=tf.truncated_normal_initializer(stddev=.1))
bias = tf.get_variable(name='bias', shape=[16], initializer=tf.truncated_normal_initializer(stddev=.1))

with tf.Session() as sess:
    # init = tf.global_variables_initializer()
    # sess.run(init)
    print(sess.run(filter_weight))


# ////////////////////////////////////////////////////////////////////////////
# LeNet-5模型
# ////////////////////////////////////////////////////////////////////////////
BATCH_SIZE = 100
x = tf.placeholder(tf.float32, shape=[ BATCH_SIZE, mnist.IMAGE_SIZE, mnist.IMAGE_SIZE, mnist.NUM_CHANNELS],
                   name='x-input')












