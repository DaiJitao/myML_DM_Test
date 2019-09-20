def getData(file):
    ss = []
    with open(file, encoding='utf-8', mode='r') as content:
        for line in content.readlines():
            sentence = line.strip()
            if len(sentence) > 1:
                ss.append(sentence[1:])
    print(" ".join(ss))


def removeDuWords(file, outfile):
    outdata = open(outfile, mode="w", encoding="utf-8")
    with open(file, mode='r', encoding="utf-8") as content:
        lines = content.readlines()
        size = len(lines)
        for i in range(1, size):
            j = i - 1
            try:
                tempFirst = lines[j].strip().split("\t")
                tempSecond = lines[i].strip().split("\t")
                if tempSecond[0] == tempFirst[0] and tempSecond[1] == tempFirst[1]:
                    pass
                else:
                    outdata.write("\t".join(tempFirst))
                    outdata.write("\n")
            except Exception as e:
                print(e)
                print(j)
                print(tempFirst)
                print(tempSecond)
    outdata.close()


def movedWords(infile, outfile):
    outdata = open(outfile, mode='w', encoding="utf-8")
    with open(infile, mode="r", encoding="utf-8") as file:
        for line in file.readlines():
            temp = line.strip().split("\t")
            if len(temp) == 3:
                if temp[1] == "还是可以" or temp[1] == "还算可以" or temp[1] == "还是可以":
                    temp[2] = '0'
                outdata.write("\t".join(temp))
            else:
                print(temp)
            outdata.write("\n")

    outdata.close()


if __name__ == "__main__":
    file = r'G:\新华网项目\汽车大数据\口碑分析\中心词搭配词\20190918\publicpraise_marked_right.txt'
    # file = r"C:\Users\dell\Desktop\去掉重复\publicpraise_marked_right.txt"
    outfile = r"G:\新华网项目\汽车大数据\口碑分析\中心词搭配词\20190918\test.txt"
    # removeDuWords(file, outfile)
    movedWords(infile=file, outfile=outfile)
