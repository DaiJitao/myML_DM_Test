from sklearn.datasets import samples_generator
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline

# 生成样本数据
X, y = samples_generator.make_classification(n_informative=4, n_features=20, n_redundant=0, random_state=5)
# 特征选择器
selector_k_best = SelectKBest(f_regression, k=10)
# 随机森林分类器
classifier = RandomForestClassifier(n_estimators=50, max_depth=4)
# 构建机器学习流水线
pipeline_classifier = Pipeline([('selector', selector_k_best), ('rf', classifier)])
# 训练分类器
pipeline_classifier.fit(X, y)
# 预测输出结果
prediction = pipeline_classifier.predict(X)
print("\nPredictions:\n", prediction)
# 评价性能
print(pipeline_classifier.score(X, y))