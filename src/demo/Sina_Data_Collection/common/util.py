import os

def mkdir(path):
    try:
        os.mkdir(path=path)
    except FileExistsError as e:
        print(e)
    except PermissionError as e:
        print(e)


def get_file(path):
    files = os.listdir(path)
    return files, len(files)

if __name__ == '__main__':
    path = "D:/scrapy/sina_data/test"
    mkdir(path)