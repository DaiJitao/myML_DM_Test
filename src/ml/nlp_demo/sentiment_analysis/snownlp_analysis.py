from snownlp import SnowNLP
import numpy as np
import pandas as pd
import pickle

fanChengCheng_score = "../scores/fanChengCheng_score.pkl"
fanChengCheng_comment = "../scores/fanChengCheng_comment.pkl"

fuChouZhe_score = "../scores/fuChouZhe_score.pkl"

jueDiQiuSheng_score = "../scores/jueDiQiuSheng_score.pkl"
zhaiTianLin_score = "../scores/zhaiTianLin_score.pkl"
zhangDanFeng_score = "../scores/zhangDanFeng_score.pkl"

dict_scores = {"fanChengCheng": fanChengCheng_score,
               "fuChouZhe": fuChouZhe_score,
               "jueDiQiuSheng": jueDiQiuSheng_score,
               "zhaiTianLin": zhaiTianLin_score,
               "zhangDanFeng": zhangDanFeng_score}


class SentimentAnalysis:
    def __init__(self, event_name):
        self.data = r"F:/scrapy/sina_data1.0.0/" + event_name + "/parsedData/all_data.csv"
        self.out_score_file = dict_scores[event_name]

    def semantic_analysis(self):
        good = pd.read_csv(self.data, header=None)
        gm = []
        save = []
        count = 1
        for comment_ in good[3]:
            try:
                score_ = SnowNLP(comment_).sentiments
            except TypeError as e:
                print(e)
                print(count)
                print(comment_)
            gm.append(score_)
            tmp = (score_, comment_)
            save.append(tmp)
            count += 1
        gm = np.array(gm)
        with open(self.out_score_file, 'wb') as pl:
            pickle.dump(gm, pl)
            print("评分已经保存")

    def data_desc(self):
        with open(self.out_score_file, 'rb') as file_:
            gm = pickle.load(file_)
        length = len(gm)
        # 0.0 - 0.2
        part1 = gm[gm <= .4]
        # 0.4 - 0.5
        part4 = gm[gm > .4]
        part4 = part4[part4 <= 0.5]
        # 0.5 - 0.6
        part5 = gm[gm > .5]
        part5 = part5[part5 <= 0.6]
        # 0.6 - 0.7
        part6 = gm[gm > .6]
        part6 = part6[part6 <= 0.7]
        # 0.7 - 0.8
        part7 = gm[gm > .7]
        part7 = part7[part7 <= 0.8]
        # > 0.8
        part8 = gm[gm > .8]
        print("0.0 - 0.4,%d,%f" % (len(part1[part1 > 0.0]), len(part1[part1 > 0.0]) / length))
        print("0.4 - 0.5,%d,%f" % (len(part4), len(part4) / length))
        print("0.5 - 0.6,%d,%f" % (len(part5), len(part5) / length))
        print("0.6 - 0.7,%d,%f" % (len(part6), len(part6) / length))
        print("0.7 - 0.8,%d,%f" % (len(part7), len(part7) / length))
        print("> 0.8,%d,%f" % (len(part8), len(part8) / length))
        # 计算好评中的正面情感平均得分
        print("正面情感平均得分,%f" % gm.mean())


def main():
    event_name = 'zhangDanFeng'
    als = SentimentAnalysis(event_name)
    # als.semantic_analysis()
    als.data_desc()


main()
