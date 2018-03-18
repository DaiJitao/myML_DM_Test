#coding:utf-8
import sklearn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

print(sklearn.__version__)
font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
print(font)

def runplt(x_and_y=None, title="匹萨价格与直径数据", x_label='直径（英寸）',
           y_label='价格（美元）'):
    plt.figure()
    plt.title(title,fontproperties=font)
    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)
    if x_and_y is None:
        x_and_y = [0, 25, 0, 25]
    if x_and_y is False:
        plt.axis()
    else:
        plt.axis(x_and_y)
    plt.grid(True)
    return plt

plt = runplt()
X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
# 创建并拟合模型
model = LinearRegression()
model.fit(X, y) # 进行拟合

# 进行预测
y_predict = model.predict(X)

if __name__=="__main__":
    plt.plot(X, y, 'r-', X, y_predict, "b--")
    plt.show()