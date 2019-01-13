import numpy as np
la = np.linalg

s1 = "I like deep learning ."
s2 = "I like NLP ."
s3 = "I enjoy flying ."

s = [s1, s2, s3]

words = ["I", "like", "enjoy", "deep", "learning", "NLP", "flying", "."]

def get_matrix(words):
    length = len(words)
    matrix = [0]*length
    for i in range(length):
        matrix[i] = [0]*length
    return matrix
print(get_matrix(words))

def demo_(s1):
    sesult = dict()
    sentence = s1
    words = sentence.split()
    for i in range(len(words) - 1):
        j = i + 1
        tmp = words[0] + "_" + words[j]
        if tmp not in result:
            resu

def get_word_times(first_word, second_word, documents):
    result = dict()
    for sentence in documents:
        words = sentence.split()
        for i in range(len(words)-1):
            j = i + 1
            tmp = words[0] + "_" + words[j]
            if tmp not in result:
                pass








def get_conn_matrix(words):
    matrix = get_conn_matrix(words)
    for i in range(len(words)):
        word = words[i]
        for j in range(len(words)):
            pass


