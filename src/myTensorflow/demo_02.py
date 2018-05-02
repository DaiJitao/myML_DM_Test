
import collections
import math
import os
import time
import random
import zipfile
import numpy as np
import urllib
import tensorflow as tf

words = "the quick brown fox jumped over the lazy dog"

url = 'http://mattmahoney.net/dc/'

def maybe_download(filename, expected_bytes):
    print("os.path: \n")
    print(os.path)
    if not os.path.exists(filename):
        filename, _ = urllib.request.urlretrieve(url + filename, filename)
    statinfo = os.stat(filename)
    if statinfo.st_size == expected_bytes:
        print('Found and verified', filename)
    else:
        print(statinfo.st_size)
        raise Exception('Failed to verify' + filename + '. Can you get to it with a browser?')
    return filename
filename = maybe_download('text8.zip', 31344016)
print("fileName");print(filename)

def read_data(filename):
    with zipfile.ZipFile(filename) as f:
        data = tf.compat.as_str(f.read(f.namelist()[0])).split()
    return data


