import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
randoms = np.random.normal(0, .05, [300, 1])
y_data = np.square(x_data) - .5 + randoms
#
# plt.plot(x_data, y_data)
# plt.show()

x_place = tf.placeholder(dtype=tf.float64, shape=[None, 1])
y_target = tf.placeholder(dtype=tf.float64, shape={None, 1})


def add_layer(x_input, input_size, out_size, acv_fun=None):
    weights = tf.Variable(tf.random_normal(dtype=tf.float64, shape=[input_size, out_size]))
    biases = tf.Variable(tf.zeros(dtype=tf.float64, shape=[1, out_size]))
    tmp = tf.add(tf.matmul(x_input, weights), biases)
    if acv_fun == None:
        return tmp
    else:
        return acv_fun(tmp)


def train(lr=.01, train_epech=1000, acv_fun =tf.nn.relu):
    losses = []
    layer1 = add_layer(x_data, input_size=1, out_size=10, acv_fun = acv_fun)
    predict = add_layer(layer1, input_size=10, out_size=1, acv_fun=None)

    loss = tf.reduce_mean(tf.reduce_sum(tf.square(predict - y_target), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(learning_rate=lr).minimize(loss)
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        for i in range(train_epech):
            sess.run(train_step, feed_dict={x_place: x_data, y_target: y_data})
            if i % 50 == 0:
                tmp = sess.run(loss, feed_dict={x_place: x_data, y_target: y_data})
                losses.append(tmp)
        # for i in losses:
        #     print("{:.9}".format(i))
        return losses


if __name__ == "__main__":
    losses1 = train(lr=.01)
    losses1_1 = train(lr=.01, acv_fun=tf.nn.elu)
    losses2 = train(lr=.1)
    losses3 = train(lr=.005)
    x = len(losses1)
    plt.plot(losses1, 'r--', label="lr=.01")
    plt.plot(losses1_1, 'g--', label="lr=.01 simoid_acv_fun")
    plt.plot(losses2, 'black', label="lr=.1")
    plt.plot(losses3, 'bo-', label='lr=.005')
    plt.legend()
    plt.grid(True)
    plt.show()
