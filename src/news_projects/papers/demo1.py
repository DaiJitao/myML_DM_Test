import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = './data.txt'

data = pd.read_table(file)

print(data)
print(data.shape)
