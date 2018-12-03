import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')



# config=tf.ConfigProto(log_device_placement=True
with tf.Session() as sess:
    print(sess.run(hello))