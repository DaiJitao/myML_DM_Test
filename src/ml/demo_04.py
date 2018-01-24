#coding;utf-8

from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()
print(digits.target[0])
print(len(digits))
print(digits.images[0])
print('Feature vector:\n', digits.images[0].reshape(-1, 64))