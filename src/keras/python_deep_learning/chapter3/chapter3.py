import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results

def to_one_hot(labels, dimension=46):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label]
    return results

def to_one_hot(train_labels, num_class):
    """ 独热编码 """
    results = np.zeros((len(train_labels), num_class))
    for i, lables in enumerate(train_labels):
        results[i, lables] = 1
    return results

data = [1,2,3,4,5] # 类别标签
data = np.array(data)

print(to_one_hot(data, 6))