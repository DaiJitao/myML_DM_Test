import jieba
import os
import chardet


class Categorization:
    def __init__(self, stop_file, input_path=None, out_path=None):
        self.stop_words = stop_file

        """ 输入路径 """
        if input_path == None:
            self.input_path = r'E:\pycharm_workspace\myML_DM_Test\resource\nlp_Data\C000010'

        """ 保存路径 """
        if out_path == None:
            self.out_path = r"E:/data/nlp_data/out_data/c00010"
        isDir = os.path.isdir(self.out_path)  # 判断有没有该路径
        if isDir == False:
            os.makedirs(self.out_path)  # 创建保存路径

    def words_segmentation(self, stop_words):
        """
        分词
        :param sentences:
        :return:
        """
        # 2 分词
        for start in range(10, 2000):
            if start % 80 == 0:
                percent = str(int((start / 1999) * 100)) + "%"
                print("正在分词", percent)
            file_name = "/" + str(start) + ".txt"
            file = self.input_path + "\\" + str(start) + ".txt"

            # test, code = self.code_detection(file)
            # if test != None:
            #     print(code)
            #     break
            # print("检查文章编码测试通过")

            text_words = []
            try:
                with open(file, 'r', encoding="GB2312", errors='ignore') as file:
                    lines = file.readlines()
                    for line in lines:
                        tmp = jieba.cut(line.strip())
                        text_words.extend([i for i in tmp if i not in data])
            except Exception as e:
                print("文件 " + file_name)
                raise e

            # 保存文件
            out_file = self.out_path + file_name
            with open(out_file, "w", encoding='utf-8') as f:  # 冲刷写的方式哦
                content = " ".join(text_words)
                f.write(content)
                # print(content)

        print("分词完毕 100% !")

    def get_stop_words(self):
        """
        获取停用词表
        :return: list
        """
        data = set()
        with open(self.stop_words, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            for i in lines:
                data.add(i.strip().replace("\n", ""))
            data.add(" ")
        return data

    def code_detection(self, file, coder="GB2312"):

        with open(file, 'rb') as f:
            data = f.read()

        if coder not in chardet.detect(data).values():
            return False
        else:
            return None, chardet.detect(data).values()

    def get_features(self):
        # 提取特征
        pass

    def get_feature_weigths(self):
        # 计算特征权值
        pass

# 选择分类模型

if __name__ == "__main__":
    cat = Categorization("./stop_words.txt")
    data = cat.get_stop_words()
    cat.words_segmentation(data)
