from collections import Counter

d = Counter([1, 2, 2])
print(d)


def f1(p, recall):
    return 2 * p * recall / (p + recall)


def get_targets(words, idx, window_size=5):
    pass


def process(text, freq=5):
    text = text.lower()


def word_2_int_(words):
    '''
    构建映射表
    :param words: []
    :return:
    '''
    vocab = set(words)
    word_to_int = {word: idx for idx, word in enumerate(vocab)}
    int_to_word = {idx: word for idx, word in enumerate(vocab)}
    return word_to_int, int_to_word


def sampleing(words):
    t = 1e-5


if __name__ == "__main__":
    words = "I love you , you love me".split(" ")
    print(words)
    print(word_2_int_(words))
