import numpy as np
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier

iris = datasets.load_iris()
x = iris["data"][:, (2, 3)]
y = (iris["target"] == 2).astype(np.float64)

svm = SVC(kernel='linear', C=1.0, random_state=0)
svm_clf = Pipeline( ( ("scaler", StandardScaler()), ("linear_svc", LinearSVC(C=1.0, loss="hinge")), ) )
model_svm = svm_clf.fit(X=x, y=y)
svm.fit(x, y)
print(model_svm)
print(svm_clf.predict([[5.5, 1.7]]))
print(svm.predict([[5.5, 1.7]]))
data = [[5.5, 1.7]]

ppn = SGDClassifier(loss="perceptron")
lr = SGDClassifier(loss="log")
svm = SGDClassifier(loss="hinge")

ppn.partial_fit(x, y, classes=np.unique(y))
lr.partial_fit(x, y, classes=np.unique(y))
svm.partial_fit(x, y, classes=np.unique(y))
print(ppn.predict(data))
print("lr ", lr.predict(data))
print("svm ", svm.predict(data))
