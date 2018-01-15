# coding:utf-8

"""
找出两个单词的最长公共子串：
例如 fish ，hish =》ish
"""

def max_len_substr(word_a, word_b):
    size_a = len(word_a)  # 作为列数
    size_b = len(word_b)  # 作为行数
    max_len = [[]] * size_b
    data = dict()
    for i in range(size_b):
        max_len[i] = [0 for i in range(size_a)]

    if size_a == size_b:
        for i in range(size_b):
            myString = ""
            if word_b[i] == word_a[i]:
                myString = myString + word_a[i]
                if i == 0:
                    max_len[i][i] = 1
                else:
                    max_len[i][i] = max_len[i - 1][i - 1] + 1
            data[max_len[i][i]] = myString
    else:
        print()
    return data


t = max_len_substr("daimmmmtao", "daummmmtao")
print(t)
