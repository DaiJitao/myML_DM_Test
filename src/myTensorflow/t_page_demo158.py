
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def f(x, a=0.5, b=0.02):
    return a * (x ** 2) + b

x_data = np.linspace(0,2,300).reshape((300,1))
print(x_data.shape)
noise = np.random.normal(0, 0.05, x_data.shape)

y_data = np.square(x_data) - 0.5 + noise

# 绘图 查看数据
"""
fig = plt.figure()
plt.plot(x_data, y_data)
plt.grid()
plt.show()
"""
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])
# 构建网络
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    bias = tf.Variable(tf.random_normal([1, out_size]))
    Wx_plus_b = tf.matmul(inputs, Weights) + bias
    if activation_function is None:
        return Wx_plus_b
    else:
        return activation_function(Wx_plus_b)
# 构建􄱤􃮣􁈖，􀘛设􄱤􃮣􁈖有10 个神经元
h1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
prediction = add_layer(h1, 10, 1, activation_function=None)

print(prediction)

# 构造损失函数
loss = tf.reduce_mean(tf.reduce_sum((ys - prediction), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
        if i % 20 == 0:
            data = sess.run(loss, feed_dict={xs:x_data, ys:y_data})
            print(data)
            print(prediction)
