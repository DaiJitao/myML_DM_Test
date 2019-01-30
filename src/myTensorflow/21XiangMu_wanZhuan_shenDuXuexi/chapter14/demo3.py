
import pickle

dataFile = "./data.txt"

with open(dataFile, "rb") as f:
    data = pickle.load(f)

print(type(data))
print(len(data))