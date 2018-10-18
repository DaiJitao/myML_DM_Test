
<<<<<<< HEAD
#coding:utf-8
import numpy as np

""" 交叉熵 衡量两个概率分布的距离"""

def cross_entropy(p, q):
    """
    p 为元组
    :param p: 正确的概率分布，实际值
    :param q: 预测的概率分布
    :return:
    """
    res = 0
    if len(p) != len(q):
        print("数据长度不一致")
        return "data error"
    for i in range(len(p)):
        p_x = p[i]
        q_x = q[i]
        res = res + p_x * np.log10(q_x)
    return -res

def soft_max(data, index):
    res = 0
    len_ = len(data)
    if len_ == 0 or index < 0:
        return 0
    # 先求分母
    temp = 0
    for i in data:
        temp += np.exp(i)
    return np.exp(data[index]) / temp


p = (1,0,0)
q1 = (.5,.4,.1)
q2 = (.8, .1, .1)

print("a ", cross_entropy(p, q1))
print("b ", cross_entropy(p, q2))
=======
import numpy
import numpy as np
import tensorflow as tf
rng = numpy.random

x = np.array([[1.,2.,3.],[4.,5.,6.]])
sess = tf.Session()

mean1 = sess.run(tf.reduce_mean(x))
mean2 = sess.run(tf.reduce_mean(x, 0))
mean3 = sess.run(tf.reduce_mean(x, 1))

print (mean1)
print (mean2)
print (mean3)


a = tf.constant(2)
b = tf.constant(3)
c = a + b
d = a + b
print(c)
print(d)
sess = tf.Session()
print(sess.run(c))
print(sess.run(d))

#
a = tf.placeholder(tf.int8)
b = tf.placeholder(tf.int8)
c = tf.add(a, b)
d = tf.multiply(a, b)
print(c)
print(d)
print(sess.run(c, feed_dict={a:2, b: 3}))
print(sess.run(d, feed_dict={a:2, b: 3}))


mat1 = tf.constant([[3,3]])
mat2 = tf.constant([[2], [2]])
print(mat1)
print(mat2)
product = tf.matmul(mat1, mat2)
print(sess.run(product))
sess.close()

# model params
learning_rate = 0.02
training_epochs = 3000
display_step=50
#
train_X = numpy.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = numpy.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]

X = tf.placeholder("float")
Y = tf.placeholder("float")

W = tf.Variable(rng.randn(), name="weights")
b = tf.Variable(rng.randn(), name="bias")

# 写公式
pred = tf.add(tf.multiply(X, W), b)

cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples) # 可以加上正则化

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X:x, Y:y})

            # Display logs per epoch step
        if (epoch + 1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
            print("Epoch:", '%04d' % (epoch + 1), "cost=", "{:.9f}".format(c),"W=", sess.run(W), "b=", sess.run(b))

    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')
>>>>>>> origin/master

