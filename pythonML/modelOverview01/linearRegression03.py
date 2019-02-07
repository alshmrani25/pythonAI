# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:07:44 2019

@author: domje

Linear Regression, Ordinary Least Squares (OLS)

- creates line that minizmizes mean squarer error between predictions and target
- OLS is the simplest (and not usually the best) unless you have lots of data

"""

from sklearn.linear_model import LinearRegression
import mglearn
from sklearn.model_selection import train_test_split



X, y = mglearn.datasets.make_wave(n_samples=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

lr = LinearRegression().fit(X_train, y_train)

print("linear coefficient")
print(lr.coef_)
print("linear intercept")
print(lr.intercept_)
print("training set score")
print(lr.score(X_train, y_train))  
print("test set score")
print(lr.score(X_test, y_test))

#Boston data
Xb, yb = mglearn.datasets.load_extended_boston()
Xb_train, Xb_test, yb_train, yb_test = train_test_split(Xb, yb, random_state = 0)
lrb = LinearRegression().fit(Xb_train, yb_train)

print("Boston training set score")
print(lrb.score(Xb_train, yb_train))  
print("Boston test set score")
print(lrb.score(Xb_test, yb_test))