
import tensorflow as tf
# 获取数据
file = "E:/data/MNIST_data_sets/"
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

y = tf.nn.softmax(tf.multiply(x , w) + b) # 预测
# 建立损失函数
y_ = tf.placeholder(tf.float32, [None, 10]) # 实际值
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])) # 损失函数
# 训练
train_step = tf.train.GradientDescentOptimizer(.5).minimize(cross_entropy)
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for i in range(100):
        batch_xs, batch_ys = mnist.train.next_batch(100)

# 验证
# 应用