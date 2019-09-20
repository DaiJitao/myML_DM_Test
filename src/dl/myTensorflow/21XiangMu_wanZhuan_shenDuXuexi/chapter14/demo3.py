import tensorflow as tf

a = tf.constant([1, 2])
b = tf.constant([1, 2])
sum_ = tf.add(a, b)

hello = tf.constant("Hello, Tensorflow!")
with tf.Session() as sess:
    h = sess.run(hello)
    print(h)
