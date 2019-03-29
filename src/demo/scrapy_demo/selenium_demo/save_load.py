import pickle
import json


def save_data_pkl(file_path, data):
    with open(file_path, "wb") as file:
        if pickle.dump(data, file=file) == None:
            print("data save success")


def load_data_pkl(file_path):
    with open(file_path, 'rb+') as file:
        return pickle.load(file)


def save_data_txt(path, data):
    with open(path, 'wb') as file:
        file.write(data)

def get_data(path):
    with open(path, 'r') as file:
        data = file.read()
        if data:
            return data
        else:
            return None

if __name__ == "__main__":
    dataPath = "F:/scrapy/xinlang/data1/page0.txt"
    text = get_data(dataPath)
    strt = text.index("(") + 1
    data = text[strt:-2]
    print(data)
    jsData = json.loads(data)
    print(jsData)


