
import numpy as np
import tensorflow as tf

x = np.array([[1.,2.,3.],[4.,5.,6.]])
sess = tf.Session()

mean1 = sess.run(tf.reduce_mean(x))
mean2 = sess.run(tf.reduce_mean(x, 0))
mean3 = sess.run(tf.reduce_mean(x, 1))

print (mean1)
print (mean2)
print (mean3)

sess.close()