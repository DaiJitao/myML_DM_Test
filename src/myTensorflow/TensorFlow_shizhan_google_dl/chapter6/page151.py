#coding:utf-8
import tensorflow as tf

# 配置参数
INPUT_NODE = 784
OUTPUT_NODE = 10

IMAGE_SIZE = 28
NUM_CHANNELS = 1
NUM_LABELS = 10

# 第一层卷积层的尺寸和深度
CONV1_DEEP = 32
CONV1_SIZE = 5

# 第二层卷积的尺寸和深度
CON2_DEEP = 32
CONV2_SIZE = 5

# 全连接层节点的个数
FC_SIZE = 512

def inference(input_tensor, train, regularizer):
    with tf.variable_scope('layer-conv1'):
        conv1_weights = tf.get_variable("weights", [CONV1_SIZE, CONV1_SIZE, NUM_CHANNELS, CONV1_DEEP],
                                        initializer=tf.truncated_normal_initializer(stddev=.1))
        conv1_biases = tf.get_variable("bias", [CONV1_DEEP], initializer=tf.truncated_normal_initializer(.0))











if __name__ == "__main__":
    # 步长 过滤器尺寸 输入图片尺寸之间的关系
    pass

