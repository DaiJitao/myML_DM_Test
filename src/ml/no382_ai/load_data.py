import json
import jieba
import time
import os

def load_data(file):
    with open(file, mode="r", encoding="utf-8") as content:
        for line in content.readlines():
            temp = line.strip()
            if len(temp) != 0:
                data = json.loads(temp)
                yield data


def load_center_words(file):
    data = []
    with open(file, mode="r", encoding="utf-8") as content:
        for line in content.readlines():
            data = data + line.strip().split(" ")
    return set(data)


def list_all_files(path):
    files = os.listdir(path)
    return files


if __name__ == "__main__":
    print(load_center_words("center_word.txt"))
    print(list_all_files(r"C:\Users\dell\Desktop\口碑数据\data\taskDir"))
# d = load_data("./test_data1.txt")
# time.sleep(1)
# for i in d:
#     print(i["content"])
# print("\n\n")
# print([word for word in jieba.cut(i["content"])])
