import csv
import json
import traceback
import time
import threading
import multiprocessing
from math import ceil
import os
from src.demo.Sina_Data_Collection.common.util import mkdir


def get_file(path):
    files = os.listdir(path)
    return files, len(files)


def save_data_to_csv(path, file_name, content):
    with open(path + file_name, mode='a', newline='') as csvfile:
        csv_write = csv.writer(csvfile, dialect="excel")
        # csv_write.writerow(["name", "age"])
        for data in content:
            try:
                csv_write.writerow(data)
            except UnicodeEncodeError as e:
                print(e)


def get_data_from_txt(filename):
    try:
        with open(file=filename, mode='r') as file:
            lines = file.read()
            return lines
    except FileNotFoundError as e:
        print(e)
        return None


def reviews_parser(content, save_path, save_file_name):
    start_index = content[0:30].index('(') + 1
    str = content[start_index:-1]
    json_data = json.loads(str)  # dict
    cmntlist = json_data['result']['cmntlist']
    if (len(cmntlist) != 0):
        result = []
        for element in cmntlist:
            uid = element['uid']
            rank = element['rank']
            area = element["area"]
            content = element['content']
            nick = element["nick"]
            parent_nick = element["parent_nick"]
            parent_uid = element['parent_uid']
            time = element['time']
            newsid = element['newsid']
            hot = element['hot']
            data = [uid, rank, area, content, nick, parent_nick, parent_uid, time, newsid, hot]
            result.append(data)
        save_data_to_csv(save_path, save_file_name, result)


def all_data_hanler(input_path, out_path, out_name, start, end):
    thread_name = threading.current_thread().getName()
    for i in range(start, end):
        name = "page" + str(i) + ".txt"
        file = input_path + name
        content = get_data_from_txt(file)
        if content != None:
            print("线程-" + thread_name + "-处理文件..." + file)
            reviews_parser(content, save_path=out_path, save_file_name=out_name)


def main():
    input_path = "F:/scrapy/sina_data/zhaiTianLin/data/"
    files, count = get_file(input_path)  # 文件的数量
    cpu_num = multiprocessing.cpu_count()
    out_path = 'F:/scrapy/sina_data/zhaiTianLin/parsedData/'
    out_name = "all_data.csv"
    interval = ceil(count / cpu_num)
    threads = []
    start = time.time()
    for i in range(cpu_num):
        start = i * interval
        end = start + interval
        thread = threading.Thread(target=all_data_hanler, args=(input_path, out_path, out_name, start, end),
                                  name=str(i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()
    inv = end - start
    print("所有数据处理完毕， 耗时：", inv)


if __name__ == '__main__':
    pass
