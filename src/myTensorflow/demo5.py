import tensorflow as tf

# config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=False)

w1 = tf.Variable(tf.random_normal([2, 3], stddev=2, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=2, seed=1))
x = tf.constant([[.7, .9]])

x_plus_w1 = tf.matmul(x, w1)
data = tf.matmul(x_plus_w1, w2)

with tf.Session() as sess:
   a = sess.run(w1.initializer)
   b = sess.run(w2.initializer)
   print(a)
   print(b)
   print(sess.run(data))