import json
import re

# pattern = re.compile(u'[^a-zA-Z\u4E00-\u9FA5]')  # 非英文字母和非汉字
pattern = re.compile(u'[\u4e00-\u9fa5]+')

regex1 = "[a-zA-Z][-a-zA-Z]{0,62}(\\.[a-zA-Z][-a-zA-Z]{0,62})+\\.?"
pattern1 = re.compile(regex1)
regex2 = "(http|ftp|https):\\/\\/[\\w\\-_]+(\\.[\\w\\-_]+)+([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?^=%&amp;/~\\+#])?"
pattern2 = re.compile(regex2)
regex3 = "[a-zA-Z0-9]"
pattern3 = re.compile(regex3)
pattern4 = re.compile(u'<[^>]+>')


def cleanData(content):
    """除去非英文字母和非汉字"""


def getArtickle(filePath, outFile):
    outData = open(outFile, encoding='utf-8', mode='w')
    with open(filePath, encoding='utf-8', mode='r') as file:
        lines = file.readlines()
        for line in lines:
            lineDict = json.loads(line.strip())
            content = lineDict.get("content").strip()
            title = lineDict.get("title").strip()
            if len(content) > 0:
                content = re.sub(pattern4, repl="", string=content)
                if len(title) > 0:
                    docs = {}
                    docs['doc'] = content
                    docs['title'] = title
                    json.dump(docs, outData, ensure_ascii=False)
                    outData.write("\n")
    outData.close()


if __name__ == "__main__":
    filePath = r"G:\新华网项目\汽车大数据\聚类实验\test_1_1567094400000_1567130400001_1567130400001_1.txt"
    out = r"G:\新华网项目\汽车大数据\聚类实验\outdata.txt"
    getArtickle(filePath, outFile=out)
    res = re.findall(pattern, '走进车内后,整个的布局相比国产车还是有很大的差距，<img   src="https://mmbiz.q')
    res = pattern.findall('走进车内后，整个的布局相比国产车还是有很大的差距，<img   src="https://mmbiz.q')
    res = pattern2.findall('走进车内后，整个的布局相比国产车还是有很大的差距，<img   src="https://mmbiz.q/>')
    print(res)
    string = '走进车内后，整个的布局相比国产车还是有很大的差距， <iframe ></iframe> />'
    res = re.sub(pattern4, repl="", string=string)
    print(res)
