import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
""" 自编码器的设计与实现 """

learning_rate = .08
trainig_epochs = 20 # 训练的轮数
batch_size = 256 # 每次训练的数据多少
display_step = 10

examples_to_show = 10

n_hidden_1 = 256
n_hidden_2 = 128
n_input = 784

X = tf.placeholder(tf.float32, [None, n_input])

weigths = {
    'encoder_h1': tf.Variable(tf.random_normal(dtype=tf.float32, shape=[n_input, n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal(dtype=tf.float32, shape=[n_hidden_1, n_hidden_2])),
    'decoder_h1': tf.Variable(tf.random_normal(dtype=tf.float32, shape=[n_hidden_2, n_hidden_1])),
    'decoder_h2': tf.Variable(tf.random_normal(dtype=tf.float32, shape=[n_hidden_1, n_input]))
}
biases = {
    'encoder_b1': tf.Variable(tf.random_normal(dtype=tf.float32, shape=[n_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal(dtype=tf.float32, shape=[n_hidden_2])),
    'decoder_b1': tf.Variable(tf.random_normal(dtype=tf.float32, shape=[n_hidden_1])),
    'decoder_b2': tf.Variable(tf.random_normal(dtype=tf.float32, shape=[n_input]))
}

def encoder(X):
    layer1 = tf.nn.sigmoid(tf.matmul(X, weigths['encoder_h1']) + biases['encoder_b1'])
    layer2 = tf.nn.sigmoid(tf.matmul(layer1, weigths['encoder_h2']) + biases['encoder_b2'])
    return layer2

def decoder(X):
    layer1 = tf.nn.sigmoid(tf.matmul(X, weigths['decoder_h1']) + biases['decoder_b1'])
    layer2 = tf.nn.sigmoid(tf.matmul(layer1, weigths['decoder_h2']) + biases['decoder_b2'])
    return layer2

encoder_op = encoder(X)
decoder_op = decoder(encoder_op)

y_pred = decoder_op
y_true = X

cost = tf.reduce_mean(tf.square(tf.subtract(y_pred, y_true)))
# tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(loss=cost)
# tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss=cost)
optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(loss=cost)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    total_batch = int(mnist.train.num_examples/batch_size)
    for epoch in range(trainig_epochs):
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            _, c = sess.run([optimizer, cost], feed_dict = {X: batch_xs})
            if epoch % display_step == 0:
                print "Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c)
    print 'finished ! '
    # 对􂌟􄆩集应用训练􀽑的自动编码网络
    encode_decode = sess.run(y_pred, feed_dict={X: mnist.test.images[:examples_to_show]})
    # 􂆨􄕗􂌟􄆩集原􀾟图􂠛和自动编码网络的􄞡建结􁵰
    f, a = plt.subplots(2, 10, figsize=(10, 2))
    for i in range(examples_to_show):
        a[0][i].imshow(np.reshape(mnist.test.images[i], (28, 28))) #􂌟􄆩集
        a[1][i].imshow(np.reshape(encode_decode[i], (28, 28))) # 􄞡建结􁵰
    f.show()
    plt.draw()
    plt.waitforbuttonpress()











