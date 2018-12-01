import tensorflow as tf
import numpy as np

x_data = np.linspace(-1, 1, 300)
x_data = x_data[:, np.newaxis]
print x_data
print x_data.shape
y_data = np.square(x_data) - .5 + noise
print y_data.shape

""" x^2 - .5 """

xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])


def add_layer(inputs, in_size, out_size, activation_function=None):
    weights = tf.Variable(initial_value=tf.random_normal(shape=[in_size, out_size], dtype=tf.float32))
    biases = tf.Variable(initial_value=tf.zeros([1, out_size]) + .1)
    w_plus_b = tf.matmul(inputs, weights) + biases
    if activation_function is None:
        return w_plus_b
    else:
        output = activation_function(w_plus_b)
        return output


# 隐层
hidden1 = add_layer(xs, 1, 20, tf.nn.relu)
# 输出层
output = add_layer(hidden1, 20, 1, None)
# 建立损失函数
loss = tf.reduce_mean(tf.reduce_sum(tf.square(output - ys), reduction_indices=[1]))  #
# 选择做优化器
train_step = tf.train.GradientDescentOptimizer(learning_rate=.1).minimize(loss)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    print
    x_data.shape
    for i in range(1000):
        train_tmp = sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i % 50 == 0:
            loss_tmp = sess.run(loss, feed_dict={xs: x_data, ys: y_data})

            print
            loss_tmp

""""  """
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 超参数
lr = .001
training_iters = 100000
batch_size = 128
# 神经网络参数
n_inputs = 28
n_steps = 28
n_hidden_units = 128
n_class = 10
# 定义输入数据和权重
x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, n_class])

weights = {
    'in': tf.Variable(tf.random_normal([n_inputs, n_hidden_units])),
    'out': tf.Variable(tf.random_normal([n_hidden_units, n_class]))
}

biases = {
    'in': tf.Variable(tf.random_normal([tf.constant(.1, shape=[n_hidden_units, ])]))
    ,
    'out': tf.Variable(tf.random_normal([tf.constant(.1, shape=[n_class, ])]))
}

def RNN(X, weights, biases):
    X = tf.reshape(X, [-1, n_inputs])
    X_in = tf.matmul(X, weights['in']) + biases['in']
    x_in = tf.reshape(X_in, [-1, n_steps, n_hidden_units])

