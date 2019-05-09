import os
import logging
import json
import re

logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='../log/get_comments.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志# a是追加模式，默认如果不写的话，就是追加模式
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式
                    )


def mkdir(path):
    try:
        os.makedirs(path)
    except FileExistsError as e:
        logging.info(e)
    except PermissionError as e:
        logging.info(e)


def list_all_files(path):
    files = os.listdir(path)
    return files, len(files)

def save_data_txt(path, data):
    with open(path, 'wb') as file:
        file.write(data)


def get_data_from_txt(filename):
    try:
        with open(file=filename, mode='r') as file:
            lines = file.read()
            return lines
    except FileNotFoundError as e:
        print(e)
        return None


def reviews_parser(content):
    if '(' not in content[0:30]:
        return []
    start_index = content[0:30].index('(') + 1
    str = content[start_index:-1]
    json_data = json.loads(str)  # dict
    if 'result' in json_data and 'cmntlist' in json_data['result']:
        cmntlist = json_data['result']['cmntlist']
        return cmntlist
    else:
        return []



def delete_file(file):
    content = get_data_from_txt(file)
    list_ = reviews_parser(content)
    try:
        if len(list_) == 0:
            if "url" not in file:
                os.remove(file)
                print("删除文件-", file)
        return True
    except:
        return False



def sort_key(s):
    if s:
        try:
            c = re.findall('\d+', s)[0]
        except:
            c = -1
        return int(c)

def strsort(alist):
    alist.sort(key=sort_key,reverse=True)
    return alist

if __name__ == '__main__':
    out_path = r"F:\scrapy\sina_data\jueDiQiuSheng\data\\"
    files, size = list_all_files(out_path)
    strsort(files)
    for i in files:
        file = out_path + i
        delete_file(file)


