

import numpy as np
from sklearn.cluster import k_means
from sklearn import metrics as mt
from matplotlib import pyplot as plt
from common.utilities import  load_data

data_file = r'E:\pycharm_workspace\myML_DM_Test\resource\python_ml_instances\Chapter04\data_multivar.txt'
data = load_data(data_file)
print(data_file)
print(type(data_file))


