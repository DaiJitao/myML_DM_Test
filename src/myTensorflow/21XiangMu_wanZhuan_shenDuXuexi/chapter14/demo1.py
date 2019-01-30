import zipfile
import time
from pprint import pprint

text8 = r"E:\data\nlp_data\text8"

def read_date(file_name):
    with open(file_name, "r") as f:
        str = f.read()
        data = str.split()
        return data

start = time.time()
data = read_date(text8)
print(data[:12])
print(len(data))
pprint(time.time() - start)