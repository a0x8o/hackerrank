#!/usr/bin/python

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

F, N = map(int, raw_input().strip().split(" "))
X = []
Y = []

for i in range(N):
    data = map(float, raw_input().strip().split(" "))
    y = data.pop()
    X.append(data)
    Y.append(y)

T = int(raw_input().strip())
X_test = []

for i in range(T):
    features = map(float, raw_input().strip().split(" "))
    X_test.append(features)

pipeline = Pipeline([('poly', PolynomialFeatures(degree=4)),
                     ('linear', LinearRegression())])

model = pipeline.fit(X, Y)
preds = model.predict(X_test)

for pred in preds:
    print(pred)
