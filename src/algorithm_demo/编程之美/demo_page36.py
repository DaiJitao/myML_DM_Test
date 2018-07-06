#coding:utf-8

def getId(data):
    count ={}
    for i in data:
        if i in count:
            count[i] =2
        else:
            count[i] = 1
    for j in count:
        if count[j] == 1:
            return j

data = ['111', '111', '222','223','222']

t = getId(data)
print(t)