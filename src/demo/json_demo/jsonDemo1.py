
import json
filePath = r'E:\pycharm_workspace\myML_DM_Test\src\demo\json_demo\backUpSet.txt'

with open(filePath, 'r', encoding="utf-8") as content:
    data = content.read()
    _data = json.dumps(data) # 将 Python 对象编码成 JSON 字符串
    print(type(_data))
    python_data = json.loads(_data) # 将已编码的 JSON 字符串解码为 Python 对象


