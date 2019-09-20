from sklearn import svm
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
import numpy as np
from sklearn.externals import joblib

# 生成测试数据
X, y = make_blobs(n_samples=100, centers=3, random_state=0, cluster_std=0.8)
print("X ", X.shape)
print("y ", y.shape)
print(X)
print(type(X))

# 构造svm分类器实例
clf_linear = svm.SVC(C=1.0, kernel='linear')
clf_poly = svm.SVC(C=1.0, kernel='poly', degree=3)
clf_rbf = svm.SVC(C=1.0, kernel='rbf', gamma=0.5)
clf_rbf2 = svm.SVC(C=1.0, kernel='rbf', gamma=0.1)

plt.figure(figsize=(10, 10), dpi=144)

clfs = [clf_linear, clf_poly, clf_rbf, clf_rbf2]
titles = ['线性核函数',
          '多项式核函数 with Degree=3',
          '高斯核函数 with gamma=0.5',
          '高斯核函数 with gamma=0.1']

# train and predict
for clf, i in zip(clfs, range(len(clfs))):
    clf.fit(X, y)
    print("{}'s score:{}".format(titles[i], clf.score(X, y)))
    out = clf.predict(X)
    print("out's shape:{}, out:{}".format(out.shape, out))
    plt.subplot(2, 2, i + 1)
    # plot_hyperplane(clf, X, y,  title=titles[i])

# 参考页面：http://scikit-learn.org/stable/modules/model_persistence.html
# http://sofasofa.io/forum_main_post.php?postid=1001002
# save trained model to disk-file
for clf, i in zip(clfs, range(len(clfs))):
    joblib.dump(clf, str(i) + '.pkl')

# load model from file and test
for i in range(len(clfs)):
    clf = joblib.load(str(i) + '.pkl')
    print("{}'s score:{}".format(titles[i], clf.score(X, y)))
