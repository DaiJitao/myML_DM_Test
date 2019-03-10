import tensorflow as tf

w = tf.Variable([[.5, 1.0]], dtype=tf.float32)
x = tf.Variable([[2.0], [1.0]], dtype=tf.float32)
d = tf.random_normal([2, 3], mean=-1, stddev=4)
y = tf.matmul(w, x)
y2 = tf.matmul(x, w)
print(y)

init = tf.global_variables_initializer()
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(init)
    print(y.eval())
    print(y2.eval())
    print(d.eval())
    path = saver.save(sess, "D:/model/test")
    print(path)

state = tf.Variable(0, dtype=tf.float32)
new_v = tf.add(state, tf.constant(1, dtype=tf.float32))
update = tf.assign(state, new_v)
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    print(sess.run(state))
    for i in range(3):
        sess.run(update)
        print(sess.run(state))


input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
y = tf.multiply(input1, input2)
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    data = sess.run(y, feed_dict={input1: 22., input2: 2.})
    print(data)


