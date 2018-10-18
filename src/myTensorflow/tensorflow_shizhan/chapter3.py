
import tensorflow as tf
# 获取数据
# file = "E:/data/MNIST_data_sets/"
file = r'F:\pycharm_workspace\myML_DM_Test\resource\tensorflowData\MNIST_data_sets'
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets(file, one_hot=True)


print("训练集" ,mnist.train.images.shape, mnist.train.labels.shape)
print("测试集",mnist.test.images.shape, mnist.test.labels.shape)
print('验证集', mnist.validation.images.shape, mnist.validation.labels.shape)
# 数据分离 测试集 训练集 验证集
print(type(mnist.validation.images))
print(mnist.validation.images[0])

x = tf.placeholder(tf.float32, [None, 784])

w = tf.Variable(tf.zeros([784, 10]))

b = tf.Variable(tf.zeros([10]))
# 建立模型

y = tf.nn.softmax(tf.matmul(x , w) + b) # 预测
# 建立损失函数
y_ = tf.placeholder(tf.float32, (None, 10)) # 实际值
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])) # 损失函数
# 训练
train_step = tf.train.GradientDescentOptimizer(.5).minimize(cross_entropy)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    i = 0
    while True:
        i += 1
        batch_xs, batch_ys = mnist.train.next_batch(60)
        data1 = sess.run(train_step, feed_dict={x:batch_xs, y_:batch_ys})
        data2 = sess.run(cross_entropy, feed_dict={x: batch_xs, y_: batch_ys})
        if i % 100 == 0:
            print(data2)
            if data2 < 0.07:
                break
    pre_w = sess.run(w)
    print(type(pre_w))
    print(pre_w[60])
    print("i:",i)




# with tf.Session() as sess:
#     tf.global_variables_initializer().run()
#     for i in range(1000):
#         batch_xs, batch_ys = mnist.train.next_batch(100)
#         train_step.run({x:batch_xs, y:batch_ys})

# 验证
# 应用