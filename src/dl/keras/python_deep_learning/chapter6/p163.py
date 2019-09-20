import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, SimpleRNN


timesteps = 100
input_features = 32
output_features = 64

inputs = np.random.random((timesteps, input_features))

print(inputs)
print(inputs.shape)

data = np.array([[1,2,3,4],[5,6,7,8],[1,2,3,4]])
print(data)
print("===========")
print(np.stack(data, axis=1))

model = Sequential()