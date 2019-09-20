from src.ml.no382_ai.load_data import list_all_files
from src.ml.no382_ai.demo1 import generate_ngram
import jieba
import json
from collections import Counter


def to_txt(file, content):
    try:
        with open(file, mode="w+", encoding="utf-8") as file:
            for tmp in content:
                file.write(tmp.__str__())
                file.write("\n")
    except:
        file.close()


def load_data(file):
    res_data = []
    with open(file, mode="r", encoding="utf-8") as content:
        for line in content.readlines():
            temp = line.strip()
            if len(temp) > 0:
                data = json.loads(temp)
                content = data['content']
                if len(content) > 6:
                    res_data.append(content)

    return res_data


def get_all_docs(path):
    path = "F:/publicpraise/taskDir/"
    files = list_all_files(path)  # 获取所有文件
    # 获取所有文档
    docs = []
    for file in files:
        fileName = "F:/publicpraise/taskDir/" + file
        tmp_docs = load_data(fileName)
        if len(tmp_docs) > 0:
            docs = docs + tmp_docs
    return docs


# 分词
def cut(content):
    """ 对每一篇文档进行分词 """
    res = [i for i in jieba.cut(content)]
    return res


def tf_idf(doc_nwords):
    # 把所有的词语转码
    pass


def combine(doc_nwords):
    all_phases = []  # 所有短语
    for doc in doc_nwords:
        for word in doc:
            phase = "".join(word).strip()
            all_phases.append(phase)
    return all_phases


if __name__ == "__main__":
    docs = get_all_docs("")
    doc_nwords = []  # n 元语法后的所有文档集合
    for doc in docs:
        # doc 文档
        res = [i for i in jieba.cut(doc)]
        nwords = generate_ngram(res, m=2)  # 生成n元词语
        if len(nwords) > 0:
            doc_nwords.append(nwords)

    all_phases = combine(doc_nwords)
    print(all_phases)
    most = Counter(all_phases).most_common()
    to_txt("result.txt", most)
