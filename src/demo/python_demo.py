from functools import reduce
import json

data = reduce(lambda x,y: x + 1, [1,2,34])
print(data)

text1 = "hadoop is easy for everybody"
text2 = "easyHadoop is open source for for for everybody"

def cout(text):
    data = dict()
    for i in text.split(" "):
        temp = 0
        if i in data:
            temp = data[i]
        data[i] = temp + 1
    return data

print(json.dumps(cout(text2)))