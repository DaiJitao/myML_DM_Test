import tensorflow as tf
from captcha.image import ImageCaptcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

character = []
# 所有大写字母
for i in range(65, 91):
    character.append(chr(i))
# 所有小写字母
for i in range(97,123):
    character.append(chr(i))
# 所有数字
for i in range(48,58):
    character.append(chr(i))
upper = character[:26]
lower = character[26:52]
number = character[52:]
charset = number


def random_captcha_text(charset=number, size=4):
    char_text = []
    for i in range(size):
        char_text.append(random.choice(charset))
    return char_text

def gen_captcha_text_and_iamge():
    image = ImageCaptcha()

    captcha_text = random_captcha_text()
    captcha_text = "".join(captcha_text)
    captcha = image.generate(captcha_text)
    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image) # 图像转换
    return captcha_text, captcha_image

text, image = gen_captcha_text_and_iamge()
print("验证码图像channel: ", image.shape)
IMAGE_HEIGHT = 60
IMAGE_WIDTH = 150
MAX_CAPTCHA = len(text)
charset_len = len(charset)


def convert2grey():
    pass

def crack_acptcha_cnn(w_alpha=.01, b_alpha=.1):
    x = tf.reshape(X, shape=[-1, IMAGE_HEIGHT * IMAGE_WIDTH, 1])
    # 3 conv layer
    w_c1 = tf.Variable(w_alpha * tf.random_normal([3, 3, 1, 32]))
    b_c1 = tf.Variable(b_alpha * tf.random_normal([32]))
    conv1 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(x, w_c1, strides=[1, 1, 1, 1], padding='SAME'), b_c1))
    conv1 = tf.nn.max_pool(conv1, ksize=[1, 2 ,2, 1], strides=[1, 2, 2, 1], padding='SAME')
    conv1 = tf.nn.dropout(conv1, keep_prob=keep_prob)

    w_c2 = tf.Variable(w_alpha * tf.random_normal([3, 3, 32, 64]))
    b_c2 = tf.Variable(b_alpha * tf.random_normal(64))
    conv2 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv1, w_c2, strides=[1, 1, 1, 1], padding='SAME')  , b_c2))
    conv2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], padding='SAME')
    conv2 = tf.nn.dropout(conv2, keep_prob)

    w_c3 = tf.Variable(w_alpha * tf.random_normal([3, 3, 64, 128]))
    b_c3 = tf.Variable(b_alpha * tf.random_normal([128]))
    conv3 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv2, w_c3, strides=[1, 1, 1, 1], padding='SAME'), b_c3))
    conv3 = tf.nn.max_pool(conv3, ksize=[1, 2, 2, 1], strides=[1, 1,1,1], padding='SAME')
    conv3 = tf.nn.dropout(conv3, keep_prob)
    # end


def train_crack_captcha_cnn():
    output = crack_acptcha_cnn()
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(output, Y))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=.001).minimize(loss)
    predict = tf.reshape(output, [-1, MAX_CAPTCHA, charset_len])
    max_idx_p = tf.argmax(output, 2)
    pass

if __name__ == "__main__":
    train = 0
    if train == 0:
        text, image = gen_captcha_text_and_iamge()
        print("验证码图像channel: ", image.shape)
        IMAGE_HEIGHT = 60
        IMAGE_WIDTH = 150
        MAX_CAPTCHA = len(text)
        charset_len = len(charset)
        X = tf.placeholder(tf.float32, [None, IMAGE_WIDTH * IMAGE_HEIGHT])
        Y = tf.placeholder(tf.float32, [None, MAX_CAPTCHA * charset_len])
        keep_prob = tf.placeholder(tf.float32) # dropout层，保留概率

        train_crack_captcha_cnn()
    if train == 1:
        IMAGE_HEIGHT = 60
        IMAGE_WIDTH = 150


