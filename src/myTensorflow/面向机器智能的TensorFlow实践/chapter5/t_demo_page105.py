
import tensorflow as tf

input_batch = tf.constant(
    [
        [[.0], [1.]],
        [[2.0], [3.]]
    ],
    [
        [[2.0], [4.]],
        [[6.0], [8.]]
    ]
)

kernel = tf.constant([
    [[1., 2.]]
])