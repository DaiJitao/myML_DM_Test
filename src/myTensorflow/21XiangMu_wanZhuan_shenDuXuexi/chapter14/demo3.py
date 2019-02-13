
import pickle

dataFile = "./data.djt"

with open(dataFile, "rb") as f:
    data = pickle.load(f)

print(type(data))
print(len(data))