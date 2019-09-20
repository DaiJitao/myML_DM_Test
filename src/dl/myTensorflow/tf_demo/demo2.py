import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

num_points = 1000
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(.0, .55)
    y1 = x1 * .1 + .3 + np.random.normal(.0, .03)
    vectors_set.append([x1, y1])

print(vectors_set)
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

print(x_data)
y_t = np.multiply(x_data, .1) + 0.3
y_t1 = np.multiply(x_data, .09) + 0.2999

plt.scatter(x_data, y_data, c = 'r')
plt.plot(x_data, y_t)
plt.plot(x_data, y_t1, c = "green")
plt.show()

w = tf.Variable(tf.random_uniform([1], -1., 1.), name='w')
b = tf.Variable(tf.zeros([1]), dtype=tf.float32, name='b')

y_predict = w * x_data + b
loss = tf.reduce_mean(tf.square(y_predict - y_data), name='loss')
loss_results = []
for rate in [.1, .2, .3, .4, .5, .6, .7]:
    res = []
    optimizer = tf.train.GradientDescentOptimizer(rate)
    train = optimizer.minimize(loss, name='train')
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        print("W=", sess.run(w), 'b=', sess.run(b), " loss=", sess.run(loss))
        for i in range(10000):
            if i % 100 == 0:
                sess.run(train)
                loss_v = sess.run(loss)
                print("W=", sess.run(w), 'b=', sess.run(b), " loss=", loss_v)
                res.append(loss_v)
    loss_results.append(res)

cout = 0
for loss_v in loss_results:
    cout += 1
    plt.plot(loss_v,label="rate:"+str(cout/10))
    plt.legend()
plt.show()





