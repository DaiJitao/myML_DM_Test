import numpy as np

# l留出验证
def simple_validation(data):
    num_validation_samples = 10000
    np.random.shuffle(data) # 打乱数据
    validation_data = data[:num_validation_samples] #定义验证集
    data = data[num_validation_samples:]
    training_data = data[:] # 定义训练集

