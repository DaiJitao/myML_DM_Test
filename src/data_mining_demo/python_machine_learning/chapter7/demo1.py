#coding:utf-8
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder #简单来说 LabelEncoder 是对不连续的数字或者文本进行编号

iris = datasets.load_iris()
X, y = iris.data[50:, [1,2]], iris.target[50:]

le = LabelEncoder()
y = le.fit_transform(y)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=1)

from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

