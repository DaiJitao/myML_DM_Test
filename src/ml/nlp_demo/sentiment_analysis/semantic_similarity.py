from simhash import Simhash
import jieba
import pandas as pd
from tools.utils import stop_words, all_index
import pickle
import os

stop_words_file = "../../data/stopWords/StopWords.txt"
stop_words_ = stop_words(stop_words_file)

''' 语义相似度 '''


class Text:
    def __init__(self, input_file=None, out_file=None):
        self.input_file = input_file
        self.out_file = out_file

    def simhash_distance(self, text1, text2):
        return Simhash(text1).distance(Simhash(text2))

    def cut_words(self, text):
        cut_text = jieba.cut(text)
        result_words = []
        for word in cut_text:
            if word not in stop_words_ and word != " ":
                result_words.append(word)
        return result_words

    def load_data_txt(self):
        result = []
        with open(self.input_file, mode='r', encoding="utf-8") as datafile:
            for line in datafile.readlines():
                result.append(line.strip())

    def load_data_csv(self):
        result = pd.read_csv(self.input_file, header=None)
        return result[3].dropna(axis=0)  # # axis=0 代表删除行 缺失值的处理


def save_data_to_local():
    ''' 分词处理 '''
    event_name = "zhangDanFeng"
    in_file = 'F:/scrapy/sina_data1.0.0/' + event_name + '/parsedData/all_data.csv'
    out_file = 'F:/scrapy/sina_data1.0.0/' + event_name + '/cutWords/comments_data.pkl'
    out_path = 'F:/scrapy/sina_data1.0.0/' + event_name + '/cutWords/'
    try:
        os.makedirs(out_path)
    except:
        pass
    text = Text(input_file=in_file)
    comments = text.load_data_csv()
    result = []
    for comment in comments:
        data = text.cut_words(comment)
        result.append(data)
    with open(out_file, 'wb') as file:
        pickle.dump(file=file, obj=result)
        print("文件保存 %s" % out_file)


''' 每一个用户的评论相似度 '''

if __name__ == "__main__":
    pass
