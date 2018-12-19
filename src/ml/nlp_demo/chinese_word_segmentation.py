
import re

def FMM(content):
    """
    正向最大匹配方法
    :param content:
    :return:
    """
    words, max_len_word = read_dict()
    word_len = len(content)
    segs = []
    if word_len <= max_len_word:
        for i in range(word_len):
            j = i
            while j < word_len:
                if content[i: (j+1)] in words:
                    segs.append(content[i: (j+1)])
                j = j + 1
    return segs



def get_content_removed_punctuation(content):
    pass


def read_dict():
    file = './dict.txt'
    word_lst = []
    max_size_word = 1
    with open(file, 'r', encoding='UTF-8') as text:
        lines = text.readlines()
        for line in lines:
            words = line.split()
            word = words[0]
            if len(word) > max_size_word:
                max_size_word = len(word)
            word_lst.append(word)
    return word_lst, max_size_word



words, __len = read_dict()
print("我在子" in words)
data = "总结改革开放的伟大成就和宝贵经验"
print(len(FMM(data)))
print(FMM(data))


