
import pandas as pd

class LoadData():
    def __init__(self, path_file):
        self.file = path_file

    def load_csv(self):
        data = pd.read_csv(self.file, header=0)  # 指定0行为头
        return data

    def load_txt(self):
        return



if __name__ == "__main__":
    file = r'D:\sys_recommand\republish_test.csv'
    load_data = LoadData(path_file = file)
    data = load_data.load_csv()