# coding;utf-8

text = "Are you curious about tokenization? Let's see how it works! We need to analyze " \
       "a couple of sentences with punctuations to see it in action."

from nltk.tokenize import sent_tokenize

sent_tokenize_list = sent_tokenize(text)
print(sent_tokenize_list)

file = r"E:\pycharm_workspace\myML_DM_Test\resource\nlp_Data\C000008\10.txt"

""" 假设词库包含三篇文档 10 11 12"""

""" 计算次词库中所有字数的总和 """
def cout_word():
    chars = []
    all_words = ''
    for i in range(10, 13):
        file = "E:\\pycharm_workspace\myML_DM_Test\\resource\\nlp_Data\C000008\\" + str(i) + ".txt"
        with open(file) as data:
            for line in data.readlines():
                all_words += line.strip()
    chars = list(all_words) # 将转换为列表
    data_set = {}
    for char in chars:
        num = chars.count(char)
        data_set[char] = num
    print(data_set)
    print("字数总和：", len(data_set))




cout_word()


