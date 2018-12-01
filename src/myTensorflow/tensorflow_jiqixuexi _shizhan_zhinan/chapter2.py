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


""" 批量训练 """
batch_size = 20
x_vals = np.random.normal(1, 0.1, 100)
y_vals = np.repeat(10., 100)
x_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
A = tf.Variable(tf.random_normal(shape=[1, 1]), dtype=tf.float32)

my_output = tf.matmul(x_data, A)
loss = tf.reduce_mean(tf.square(y_target - my_output))

my_opt = tf.train.GradientDescentOptimizer(learning_rate=.01)
train_step = my_opt.minimize(loss)

loss_batch = []
with tf.Session() as sess:
    init = tf.global_variables_initializer() # 初始化A
    sess.run(init)
    for i in range(100):
        rand_index = np.random.choice(100, size=batch_size)
        rand_x = np.transpose(x_vals[rand_index])
        rand_y = np.transpose(y_vals[rand_index])
        rand_x = np.mat(rand_x).transpose()
        rand_y = np.mat(rand_y).transpose()

        sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
        if (i + 1) % 50 == 0:
            temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
            print ("A=", sess.run(A), " loss=", temp_loss)
            loss_batch.append(temp_loss)

""" 随机训练 """
""" 随机梯度训练 """
loss_sto = []
with tf.Session() as sess:
    init = tf.global_variables_initializer() # 初始化A
    sess.run(init)
    for i in range(1000):
        rand_index = np.random.choice(100)
        rand_x = np.transpose(x_vals[rand_index])
        rand_y = np.transpose(y_vals[rand_index])
        rand_x = np.mat(rand_x).transpose()
        rand_y = np.mat(rand_y).transpose()

        sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
        if (i + 1) % 5 == 0:
            temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
            # print "A=", sess.run(A), " loss=", temp_loss
            loss_sto.append(temp_loss)

""" end 随机 """
""" 创建分类器 """
from sklearn import datasets
iris = datasets.load_iris()
iris_data = iris.data
iris_target = iris.target
batch_size = 20

binary_target = np.array([1. if x==0 else .0 for x in iris_target])
iris_2d = np.array([ [x[2], x[3]]for x in iris_data] )

x2_data = tf.placeholder(dtype=tf.float32, shape=[None, 1])
x1_data = tf.placeholder(dtype=tf.float32, shape=[None, 1])
A = tf.Variable(tf.random_normal(shape=[1,1]), dtype=tf.float32)
b = tf.Variable(tf.random_normal(shape=[1,1]), dtype=tf.float32)
y_target = tf.placeholder(dtype=tf.float32, shape=[None, 1])

my_mult = tf.matmul(x2_data, A)
my_add = tf.add(my_mult, b)
my_output = tf.subtract(x1_data, my_add)

xentroy = tf.nn.sigmoid_cross_entropy_with_logits(logits=my_output, labels = y_target)
my_opt = tf.train.GradientDescentOptimizer(learning_rate=.05)
train_step = my_opt.minimize(xentroy)

loss_batch = []
with tf.Session() as  sess:
    init = tf.global_variables_initializer()
    # init = tf.initialize_all_variables()
    sess.run(init)
    for i in range(1000):
        rand_index = np.random.choice(150, batch_size) #随机选在20个数
        y_vals = binary_target[rand_index] # 此为（20， ）
        x_vals = iris_2d[rand_index]
        x2_vals = x_vals[:, 1]
        x1_vals = x_vals[:, 0]
        # 转换为（None, 1)矩阵
        x1_vals = np.mat(x1_vals).transpose()
        x2_vals = np.mat(x2_vals).transpose()
        y_vals = np.mat(y_vals).transpose()
        sess.run(train_step, feed_dict={x2_data: x2_vals, x1_data:x1_vals, y_target:y_vals})
        if (i +1) % 50 == 0:
            temp_loss = sess.run(xentroy, feed_dict={x2_data: x2_vals, x1_data:x1_vals, y_target:y_vals})
            pramas_A = sess.run(A)
            pramas_b = sess.run(b)
            print ("loss=", temp_loss, " A=", pramas_A, " b=", pramas_b)
            loss_batch.append(temp_loss)


""" 创建分类器 随机梯度下降"""
from sklearn import datasets
iris = datasets.load_iris()
iris_data = iris.data
iris_target = iris.target
batch_size = 1
# 迭代次数
num_ites = 10000
num_print = 500

binary_target = np.array([1. if x==0 else .0 for x in iris_target])
iris_2d = np.array([ [x[2], x[3]]for x in iris_data] )

x2_data = tf.placeholder(dtype=tf.float32, shape=[None, 1])
x1_data = tf.placeholder(dtype=tf.float32, shape=[None, 1])
A = tf.Variable(tf.random_normal(shape=[1,1]), dtype=tf.float32)
b = tf.Variable(tf.random_normal(shape=[1,1]), dtype=tf.float32)
y_target = tf.placeholder(dtype=tf.float32, shape=[None, 1])

my_mult = tf.matmul(x2_data, A)
my_add = tf.add(my_mult, b)
my_output = tf.subtract(x1_data, my_add)

xentroy = tf.nn.sigmoid_cross_entropy_with_logits(logits=my_output, labels = y_target)
my_opt = tf.train.GradientDescentOptimizer(learning_rate=.05)
train_step = my_opt.minimize(xentroy)

loss_batch = []
A_batch = []
b_batch = []
with tf.Session() as  sess:
    init = tf.global_variables_initializer()
    # init = tf.initialize_all_variables()
    sess.run(init)
    for i in range(num_ites):
        rand_index = np.random.choice(150) #随机选在20个数,批量梯度下降
        y_vals = binary_target[rand_index] # 此为（20， ）
        x_vals = iris_2d[rand_index, :] # 选择某一行
        x2_vals = np.mat(x_vals[1])
        x1_vals =  np.mat(x_vals[0])
        y_vals = np.mat(y_vals)
        sess.run(train_step, feed_dict={x2_data: x2_vals, x1_data:x1_vals, y_target:y_vals})
        if (i + 1) % num_print == 0:
            temp_loss = sess.run(xentroy, feed_dict={x2_data: x2_vals, x1_data:x1_vals, y_target:y_vals})
            pramas_A = sess.run(A)
            pramas_b = sess.run(b)
            print("loss=", str(temp_loss), " A=", str(pramas_A), " b=", str(pramas_b))
            loss_batch.append(temp_loss[0, 0])
            A_batch.append(pramas_A[0, 0])
            b_batch.append(pramas_b[0, 0])
# 绘图
import matplotlib.pyplot as plt
x = range(0, num_ites, num_print)
plt.plot(x, loss_batch, "r-", label="loss batch")
plt.plot(x, A_batch, "b-", label="A")
plt.plot(x, b_batch, "bs-", label="b_batch")
plt.legend()
plt.show()
""" end  """

tf.nn.conv2d(x_data, filter=[], strides=[], padding='', name='')
tf.nn.max_pool()





