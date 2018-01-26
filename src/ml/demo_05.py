
import pandas as pd
df = pd.read_csv(r'C:\Users\daijitao\Downloads\smsspamcollection\SMSSpamCollection.csv',
                 delimiter='\t', header=None)

print(df.head())
print('含spam短信数量：', df[df[0] == 'spam'][0].count())
print('含ham短信数量：', df[df[0] == 'ham'][0].count())

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split

print(df.head(10))

X_train_raw, X_test_raw, y_train, y_test = train_test_split(df[1], df[0])
print(X_train_raw)
print(X_test_raw)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)

# for i, prediction in enumerate(predictions[-5:]):
#     print('预测类型 %s. 信息：%s' (prediction, X_test_raw.iloc[i]))
print(len(predictions))
print(predictions.shape)
for i in predictions:
    print(i)