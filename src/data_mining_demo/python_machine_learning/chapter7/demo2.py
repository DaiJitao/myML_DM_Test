from sklearn import preprocessing

le = preprocessing.LabelEncoder()
le.fit(["Japan", "china", "Japan", "Korea", "china"])
print('标签个数:%s' % le.classes_)
print('标签值标准化:%s' % le.transform(["Japan", "china", "Japan", "Korea", "china"]))
print('标准化标签值反转:%s' % le.inverse_transform([0, 2, 0, 1, 2]))
