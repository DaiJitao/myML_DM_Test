import tensorflow as tf




hello = tf.constant('hhh')

with tf.device("/cpu:0"):
    sess = tf.Session()
    print(sess.run(hello))
    sess.close()
