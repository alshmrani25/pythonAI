# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:54:33 2019

@author: domje

Ridge Regression, similar to OLS, but different coefficient calculation

"""

import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Boston data
Xb, yb = mglearn.datasets.load_extended_boston()
Xb_train, Xb_test, yb_train, yb_test = train_test_split(Xb, yb, random_state = 0)
ridge = Ridge().fit(Xb_train, yb_train)

print("Boston training set score")
print(ridge.score(Xb_train, yb_train))  
print("Boston test set score")
print(ridge.score(Xb_test, yb_test))

#adjusting alpha gives results depending on data set...
ridge10 = Ridge(alpha=10).fit(Xb_train, yb_train)
print("Boston10 training set score")
print(ridge10.score(Xb_train, yb_train))  
print("Boston10 test set score")
print(ridge10.score(Xb_test, yb_test))

ridge01 = Ridge(alpha=0.1).fit(Xb_train, yb_train)
print("Boston01 training set score")
print(ridge01.score(Xb_train, yb_train))  
print("Boston01 test set score")
print(ridge01.score(Xb_test, yb_test))


#adding this back just so we can show it in the graph...
lrb = LinearRegression().fit(Xb_train, yb_train)

plt.plot(ridge.coef_, 's', label="Ridge alpha = 1.0")
plt.plot(ridge10.coef_, '^', label="Ridge alpha = 10")
plt.plot(ridge01.coef_, 'v', label="Ridge alpha = 0.1")

plt.plot(lrb.coef_, 'o', label="Linear Regression")
plt.xlabel("Coefficient index")
plt.ylabel("Coefficient magnitude")
plt.hlines(0, 0, len(lrb.coef_))
plt.ylim(-25, 25)
plt.legend()

