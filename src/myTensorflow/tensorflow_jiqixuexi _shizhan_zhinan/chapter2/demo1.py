import tensorflow as tf

data = tf.constant([-1, 2], dtype=tf.float32)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    b = tf.nn.relu(data)
    c = sess.run(b)
    cc = sess.run(tf.nn.softplus(data))
    print(b)
    print(c)
    print(cc)