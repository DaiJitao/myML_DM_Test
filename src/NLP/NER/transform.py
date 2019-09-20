import codecs
import sys


def character_tagging(input_file, output_file):
    input_data = codecs.open(input_file, mode='r', encoding='utf-8')
    out_data = codecs.open(output_file, mode='w', encoding='utf-8')

    for line in input_data.readlines():
        words = line.strip().split()
        for word in words:
            word = word.replace("/", "    ")
            out_data.write(word + "\n")

    input_data.close()
    out_data.close()


def combine_nr_words(words, tag='nr'):
    newwords = []

    for word in words:
        word_tag = word.split("/")
        tag = word_tag[1]
        word = word_tag[0]
        if tag == tag:
            newwords.append()


def combine_nr_words_test(words, tag='nr'):
    temp = ''
    newwords = []
    size = len(words)
    for i in range(size):
        word = words[i]
        if word == tag:
            if i == 0:
                newwords.append({tag: word})
            else:
                tagDict = newwords[i - 1]
                tagDict.get(tag) == None

    return newwords


def transform_data(inputfile, outfile):
    ''' 人民日报语料库的创建 '''
    outdata = open(outfile, mode='w', encoding='utf-8')
    with open(inputfile, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            words = [word for word in line.strip().split(" ") if len(word) > 0][1:]  # 剔除第一列
            print(words)
            break
            if len(words) > 1:
                for word in words:
                    word_tag = word.split("/")
                    # 非人名
                    if word_tag[1] != "nr":
                        word = word_tag[0]
                        if len(word) == 1:  # 单个词
                            outdata.write(word + "    " + "S" + "    " + "O\n")
                        else:
                            size = len(word)
                            for i in range(size):
                                if i == 0:
                                    tag = 'B'
                                elif i == (size - 1):
                                    tag = "E"
                                else:
                                    tag = "M"
                                outdata.write(word[i] + "   " + tag + "    " + "O\n")
                    else:  # 人名
                        pass


if __name__ == "__main__":
    inputfile = r'F:\pycharm_workspce\myML_DM_Test\src\NLP\NER\data\ren_min\199801.txt'
    # transform_data(inputfile=inputfile, outfile="./data/train_out.txt")
    words = ["1", "1", "1", "2", "2", "1", "1"]
    print(combine_nr_words_test(words, '1'))
