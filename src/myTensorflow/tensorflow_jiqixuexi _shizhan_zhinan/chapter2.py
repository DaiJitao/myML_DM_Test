import numpy as np
import tensorflow as tf

x_vals = np.array([1., 2., 3., 4., 5.])
x_data = tf.placeholder(tf.float32)
my_const = tf.constant(3.)
my_product = x_vals * my_const
with tf.Session() as sess:
    for x_val in x_vals:
        tmp = sess.run(my_product, feed_dict={x_data: x_val})
        print(tmp)

x_data = tf.placeholder(tf.float32, [3, 5])
# 定义常数
m1 = tf.constant([[1.], [2.], [3.], [4.], [5.]])
m2 = tf.constant([[2.]])
a1 = tf.constant([[10.]])

# 定义操作
prod1 = tf.matmul(x_data, m1)
prod2 = tf.matmul(prod1, m2)
add1 = tf.add(prod2, a1)
with tf.Session() as sess:
    for x_val in x_vals:
        data = sess.run(add1, feed_dict={x_data: x_val})
        print(data)


# -----------------------------------------------------------------------------------------
# page129
""" 已知 f(x) = ax, 其目标值为50， 求参数a? """

a = tf.Variable(tf.constant(4.0))
x_val = 5.0
x_data = tf.placeholder(tf.float32)
w1 = tf.multiply(a, x_data)
loss = tf.square(tf.subtract(w1, 50.)) # L2正则化

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    my_opt = tf.train.GradientDescentOptimizer(.01)
    train_step = my_opt.minimize(loss)
    for i in range(10):#训练次数
        sess.run(train_step, feed_dict={x_data:x_val})
        a_val = sess.run(a)       # 打印参数a
        mult_output = sess.run(w1, feed_dict={x_data:x_val})
        print("a = " + str(a_val) + " output=" + str(mult_output))


