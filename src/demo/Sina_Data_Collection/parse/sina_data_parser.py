import csv
import json
import traceback
import time
import threading
import multiprocessing
from multiprocessing import Queue
from math import ceil
import os
from src.demo.Sina_Data_Collection.common.util import mkdir
import logging

logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='./log/parser.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志# a是追加模式，默认如果不写的话，就是追加模式
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式
                    )


def get_file(path):
    files = os.listdir(path)
    return files, len(files)


def get_data_from_txt(filename):
    try:
        with open(file=filename, mode='r') as file:
            lines = file.read()
            return lines
    except FileNotFoundError as e:
        print(e)
        return None


def save_data_to_csv(path, file_name, res_queue):
    """
    :param path: 保存路径
    :param file_name: 文件名字
    :param res_queue:
    :return:
    """
    with open(path + file_name, mode='a', newline='') as csvfile:
        csv_write = csv.writer(csvfile, dialect="excel")
        # csv_write.writerow(["name", "age"])
        while not res_queue.empty():
            content = res_queue.get()
            print("队列大小", res_queue.qsize())
            for data in content:
                try:
                    csv_write.writerow(data)
                except UnicodeEncodeError as e:
                    print("编码错误：", e)
                    logging.info(e)


def reviews_parser(content, res_queue, file):
    """
    解析文件，提取数据
    :param content:
    :return:
    """
    if "(" in content[0:30]:
        start_index = content[0:30].index('(') + 1
        str = content[start_index:-1]
        json_data = json.loads(str)  # dict
        if 'result' in json_data and 'cmntlist' in json_data['result']:
            cmntlist = json_data['result']['cmntlist']
        else:
            cmntlist = []
        if (len(cmntlist) != 0):
            result = []
            for element in cmntlist:
                uid = element['uid']
                rank = element['rank']
                area = element["area"]
                content_ = element['content']
                nick = element["nick"]
                parent_nick = element["parent_nick"]
                parent_uid = element['parent_uid']
                time = element['time']
                newsid = element['newsid']
                hot = element['hot']
                data = [uid, rank, area, content_, nick, parent_nick, parent_uid, time, newsid, hot]
                result.append(data)
            res_queue.put(result)

    else:
        pass


def all_data_hanler(input_path, start, end, res_queue):
    thread_name = threading.current_thread().getName()
    for i in range(start, end):
        name = "page" + str(i) + ".txt"
        file = input_path + name
        content = get_data_from_txt(file)  # 读取文件
        if content != None:
            # print("\n线程-" + thread_name + "-处理文件..." + file)
            logging.info("\n线程-" + thread_name + "-处理文件..." + file)
            reviews_parser(content, res_queue, file)


def main():
    event_name = 'jueDiQiuSheng'
    input_path = "F:/scrapy/sina_data/"+ event_name +"/data/"
    out_path = "F:/scrapy/sina_data/" + event_name + "/parsedData/"
    out_name = "all_data.csv"

    res_queue = Queue()  # 队列
    files, count = get_file(input_path)  # 文件的数量
    cpu_num = multiprocessing.cpu_count()
    interval = ceil(count / cpu_num)
    threads = []
    start = time.time()
    mkdir(out_path)
    for i in range(cpu_num):
        start = i * interval
        end = start + interval
        thread = threading.Thread(target=all_data_hanler, args=(input_path, start, end, res_queue),
                                  name=str(i))  # 解析数据线程
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()
    # save_thread = threading.Thread(target=save_data_to_csv, args=(out_path, out_name, res_queue))  # 保存文件线程
    # save_thread.start()
    # save_thread.join()
    save_data_to_csv(out_path, out_name, res_queue)
    print("start-", start, " end-", end)
    end = time.time()
    inv = end - start
    print("所有数据处理完毕， 耗时：", inv)
    logging.info("所有数据处理完毕， 耗时：" + str(inv))


if __name__ == '__main__':
    main()
