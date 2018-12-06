# 单层神经网络的实现
import numpy as np
from sklearn import datasets
import tensorflow as tf

def normalize(m):
    """ 标准化 [0, 1]"""
    xmin = np.min(m)
    xmax = np.max(m)
    tmp = m - xmin
    return tmp / (xmax - xmin)

def add_layer(val, acv_fun=None):
    if acv_fun == None:
        return val
    else:
        return acv_fun(val)


iris = datasets.load_iris()
iris_data = iris.data
x_vals = np.array([x[0:3] for x in iris_data])
y_vals = np.array([x[3] for x in iris_data])
batch_size = 50
# 80% 训练集 20%测试集
all_size = len(x_vals)
train_size = round(all_size * .8)

seed = 2
tf.set_random_seed(seed)
np.random.seed(seed)

train_index = np.random.choice(all_size, train_size, replace=False) # 获取训练集的下标
test_index = list(set(np.arange(all_size)) - set(train_index)) # 获取测试集下标
# 获取训练集
x_vals_train = x_vals[train_index]
y_vals_train = y_vals[train_index].reshape(-1, 1)

x_vals_train = normalize(x_vals_train)
y_vals_train = normalize(y_vals_train)
# 获取测试集
y_vals_test = y_vals[test_index]
x_vals_test = x_vals[test_index]

x_data = tf.placeholder(dtype=tf.float32, shape=[None, 3])
y_target = tf.placeholder(dtype=tf.float32, shape=[None, 1])

# 隐层 共5个节点
hidden_weights = tf.Variable(dtype=tf.float32, initial_value = tf.random_normal(stddev=1, mean=0, shape=[3, 5]))
hidden_biases = tf.zeros(dtype=tf.float32, shape=[5])
output_weights = tf.Variable(dtype=tf.float32, initial_value = tf.random_normal(stddev=1, mean=0, shape=[5, 1]))
output_biases = tf.zeros(dtype=tf.float32, shape=[1])
# 定义网络
val1 = tf.add(tf.matmul(x_data, hidden_weights),  hidden_biases)
hidden_layer = add_layer(val=val1, acv_fun=tf.nn.relu)
val2 = tf.add(tf.matmul(hidden_layer, output_weights), output_biases)
out_layer = add_layer(val2, tf.nn.relu)

#定义优化器
loss = tf.reduce_mean(tf.square(out_layer - y_target))
opt = tf.train.GradientDescentOptimizer(learning_rate=.001).minimize(loss)

print(x_vals_train)
print(y_vals_train.shape)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    n = len(x_vals_train)
    for i in range(1000):
        random_index = np.random.choice(n, batch_size)
        x_random_vals = x_vals_train[random_index]
        y_random_vals = y_vals_train[random_index]
        sess.run(opt, feed_dict={x_data: x_random_vals, y_target: y_random_vals})
        loss_tmp = sess.run(loss, feed_dict={x_data: x_random_vals, y_target: y_random_vals})
        if i % 5 == 0:
            print(i)









