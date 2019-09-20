import time
import numpy as np
import tensorflow as tf
import random
from collections import Counter

textFile = 'data/Javasplittedwords'  # 数据清理之后的文本


def getText(textFile):
    with open(textFile, mode='r', encoding="utf-8") as file:
        text = file.read()
    return text


def word2int(words):
    vocab = set(words)
    word_to_int = {word: idx for idx, word in enumerate(vocab)}
    int_to_word = {idx: word for idx, word in enumerate(vocab)}
    return word_to_int, int_to_word


def negSampling(int_words, t=1e-5, threshold=.9, words_count=None):
    """
    负采样
    :param t:
    :param threshold:
    :return:
    """
    total_count = len(int_words)
    if words_count == None:
        int_word_counts = Counter(int_words)
    else:
        int_word_counts = words_count
    # 计算单词频率
    word_freqs = {w: c / total_count for w, c in int_word_counts.items()}
    # 计算被删除的概率
    prob_drop = {w: 1 - np.sqrt(t / word_freqs[w]) for w in int_word_counts}
    # 对单词进行采样
    train_words = [w for w in int_words if prob_drop[w] < threshold]
    return train_words


def get_targets(words, idx, window_size=5):
    '''
    获得input word的上下文单词列表

    参数
    ---
    words: 单词列表
    idx: input word的索引号
    window_size: 窗口大小
    '''
    target_window = np.random.randint(1, window_size + 1)
    # 这里要考虑input word前面单词不够的情况
    start_point = idx - target_window if (idx - target_window) > 0 else 0
    end_point = idx + target_window
    # output words(即窗口中的上下文单词)
    targets = set(words[start_point: idx] + words[idx + 1: end_point + 1])
    return list(targets)


def get_batches(words, batch_size, window_size=5):
    '''
    构造一个获取batch的生成器
    '''
    n_batches = len(words) // batch_size

    # 仅取full batches
    words = words[:n_batches * batch_size]

    for idx in range(0, len(words), batch_size):
        x, y = [], []
        batch = words[idx: idx + batch_size]
        for i in range(len(batch)):
            batch_x = batch[i]
            batch_y = get_targets(batch, i, window_size)
            # 由于一个input word会对应多个output word，因此需要长度统一
            x.extend([batch_x] * len(batch_y))
            y.extend(batch_y)
        yield x, y


def main() -> None:
    words = getText(textFile).split(" ")
    # 筛选掉低频单词
    words_count = Counter(words)
    words = [word for word in words if words_count[word] > 50]
    (word_to_int, _) = word2int(words)
    # 单词转换为数字
    int_words = [word_to_int[word] for word in words]
    # ===============
    train_graph = tf.Graph()
    with train_graph.as_default():
        inputs = tf.placeholder(dtype=tf.int32, shape=[None], name='inputs')
        output = tf.placeholder(dtype=tf.int32, shape=[None, None], name='outputs')


def demo(dai: int = 2) -> str:
    print(dai)
    print("和咯哦")
    tf.nn.conv2d()


def demoConv2d(input):
    filter_weighs = tf.Variable(tf.truncated_normal(name='filter', shape=[3, 3, 3, 500], stddev=.01))
    bs = tf.Variable(tf.truncated_normal(name='bs', shape=[1, 500], stddev=.01))

    conv = tf.nn.conv2d(input, filter=filter_weighs, strides=[1, 1, 1, 1], padding='SAME')
    result = tf.nn.bias_add(conv, bs)
    return tf.nn.relu(result)


if __name__ == "__main__":
    m = demo(6)
    print(m)
