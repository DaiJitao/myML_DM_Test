# coding;utf-8

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

df = pd.read_csv("")
X = df[list(df.colums)]
Y = []
regressor = LinearRegression()
X_train, X_test, Y_train, Y_test = regressor.fit(X, Y)

y_predictions = regressor.predict(X_test)