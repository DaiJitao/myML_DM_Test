import json
import jieba
import time


def load_data(file):
    with open(file, mode="r", encoding="utf-8") as content:
        for line in content.readlines():
            data = json.loads(line)
            yield data


def load_center_words(file):
    data = []
    with open(file, mode="r", encoding="utf-8") as content:
        for line in content.readlines():
            data = data + line.strip().split(" ")
    return set(data)


if __name__ == "__main__":
    print(load_center_words("center_word.txt"))
# d = load_data("./test_data1.txt")
# time.sleep(1)
# for i in d:
#     print(i["content"])
# print("\n\n")
# print([word for word in jieba.cut(i["content"])])
