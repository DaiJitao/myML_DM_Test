
def read_file_lines(path, nmax = 0):
    fp = open(path, 'rb')
    ncount = 0
    while True:
        content = fp.readlines()
        if content == "" or (ncount >= nmax and nmax != 0):
            break
        yield content
        if nmax != 0:
            ncount += 1
    fp.close()

path = r'E:\pycharm_workspace\myML_DM_Test\resource\tensorflow_JiQiXueXi_ShiZhanZhiNan\readMe.txt'

data = read_file_lines(path, nmax= 10)
print(data)
for i in data:
    print(type(i))
    print(len(i))
    if len(i) > 0:
        print(i[0].decode('utf-8'))

