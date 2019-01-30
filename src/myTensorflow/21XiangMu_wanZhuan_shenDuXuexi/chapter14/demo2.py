import pickle

data = [12, 13]

path = "E:/data/text.txt"

with open(path, 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

with open(path, 'rb') as f:
    d = pickle.load(f)
    print(type(d))
    print(d)