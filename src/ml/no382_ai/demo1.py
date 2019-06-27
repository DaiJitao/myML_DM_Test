import re
import jieba
from collections import Counter

# ***********************************************************************
# 车漆很薄
#
# 车皮也很薄
# ***********************************************************************

# 因为不知道名词性短语的长度，所以分别采取2元、3元、4元和5元模型

pattern = re.compile(u'[^a-zA-Z\u4E00-\u9FA5]')  # 非英文字母和非汉字


def demo():
    tt = "华虹NEC是以日本NEC作为技术合作方的中国第一条0.35微米、8英寸超大规模集成电路生产线项目。我" \
         "负责包括洁净室空调系统,冷冻机系统,工艺设备冷却水系统等7个系统的控制系统,具体职责涉及从系统的建立到运行到维护到改进整个流程." \
         " * 负责空调等系统的招标及评标工作 * 编制合同技术条款 * 制作项目工程计划及进度控制 * 协调分包商 * 制定设备维护计划 * 动力控制系统运行分析" \
         "及改进 * 动力控制设备维护 * 制定设备维护预算及成本控制 * 制定测量仪器管理条例及负责日常管理"

    resutl = re.findall(pattern, tt)
    print(pattern.findall(tt))
    return resutl


# 1.1 分词
def cut(file="text.txt"):
    data = [line.strip() for line in open(file, encoding='utf-8', mode='r') if
            "RESUMEDOCSSTARTFLAG" not in line and len(line.strip()) > 0]
    res = [list(jieba.cut(line)) for line in data]
    return res


# 1.2 n元语法模型的生成
# ngram
def generate_ngram(sentence, n=7, m=2):
    """ n元模型  m最小值"""
    if len(sentence) < n:
        n = len(sentence)
    result = [tuple(sentence[i - k: i]) for k in range(m, n + 1) for i in range(k, len(sentence) + 1)]
    result = [item for item in result if
              len("".join(item).strip()) > 1 and len(pattern.findall("".join(item).strip())) == 0]
    return result


def extract_frequence_phrases():
    ''' 提取高频短语 '''
    data = [line.strip() for line in open("text.txt", encoding='utf-8', mode='r')
         if "RESUMEDOCSSTARTFLAG" not in line and len(line.strip()) > 0]

    # data = [generate_ngram(sentence) for sentence in cut("text2.txt")] # file read 分词
    doc_words = []
    words_set = set()
    words = []
    for i in data:
        d = ["".join(t).strip() for t in i]
        doc_words.append(d)
        for word in d:
            words_set.add(word)
            words.append(word)

    # 统计每一个词的频次
    print(words_set)
    print(words)
    print(words.count('快速消费品'))
    d = Counter(words).most_common(90) #提取前五十个
    print(len(d))
    print(d)

extract_frequence_phrases()

list.sort()
