import matplotlib.pyplot as plt

data = [1, 1, 0, 0, -1, 0, 1, 1, -1]

def print_plot(a, is_ = True):
    plt = a
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码问题
    plt.rcParams['axes.unicode_minus'] = is_
    plt.plot(data, ":", marker='o')
    plt.grid(True, axis='both')
    plt.title("技术测试")
    plt.show()

plt.figure(1)
axes1 = plt.subplot(211)
axes2 = plt.subplot(212)
axes1.plot(data)

axes1 = plt.subplot(211)
axes2 = plt.subplot(212)
axes1.plot(data)
axes2.plot(data)
plt.show()