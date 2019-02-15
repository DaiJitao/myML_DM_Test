import pickle
import numpy as np
import pandas as pd

datafile = "./cleanedData.dai"

with open(datafile, 'rb') as file:
    dataset = pickle.load(file)

print(dataset.head())