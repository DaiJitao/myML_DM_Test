import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

with tf.Session() as sess:
    x_vals = np.random.normal(1, .1, 100)
    y_vals = np.repeat(10, 100)
