"""
构建机器学习流水线
"""
from sklearn.datasets import samples_generator
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline

X, y = samples_generator.make_classification(n_informative=4, n_features=20, n_redundant=0, random_state=5)
print(X)
print(len(X))
print(y)
print(len(y))
# selector_k_best = SelectKBest(f_regression, k=10)
#
# classifier = RandomForestRegressor(n_estimators=20, max_depth=4)
# pipeline_classifier = Pipeline([('selector', selector_k_best), ('rf', classifier)])
#
# pipeline_classifier.set_params(selector__k = 6, rf__n_estimators = 25)
#
# pipeline_classifier.fit(X, y)
# prediction = pipeline_classifier.predict(X)
# print("Predisction: ", prediction)
# # 打印分类器得分, 模型评价
# print("Score: ", pipeline_classifier.score(X, y))