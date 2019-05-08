import os

def mkdir(path):
    try:
        os.makedirs(path)
    except FileExistsError as e:
        print(e)
    except PermissionError as e:
        print(e)


def get_file(path):
    files = os.listdir(path)
    return files, len(files)

def save_data_txt(path, data):
    with open(path, 'wb') as file:
        file.write(data)

if __name__ == '__main__':
    out_path = 'F:/scrapy/sina_data/zhaiTianLin/data/'
    mkdir(out_path)