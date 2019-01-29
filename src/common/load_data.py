
import pandas as pd

class LoadData():
    def __init__(self, path_file=None):
        self.file = path_file

    def load_csv(self, file=None):
        if file != None:
            self.file = file
        data = pd.read_csv(self.file, header=0)  # 指定0行为头
        return data

    def load_txt(self, path):
        """ 读取文本文件 """
        result = ""
        with open(path, 'r', ) as tf:
            lines = tf.readlines()
            for line in lines:
                result += line.strip()
        return result



if __name__ == "__main__":
    file = r'D:\sys_recommand\republish_test.csv'
    load_data = LoadData(path_file = file)
    data = load_data.load_csv()

    path = r"E:\pycharm_workspace\myML_DM_Test\resource\nlp_Data\C000008\10.txt"
    content = load_data.load_txt(path)
    print(content)