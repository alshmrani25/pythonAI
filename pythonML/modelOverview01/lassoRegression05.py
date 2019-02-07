# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 12:18:46 2019

@author: domje

Lasso Linear Regression
- also tries to get coeffients close to zero
- some end up as 0 (and are ignored)
- bad model unless you have very large number of features, and only expect some to be important


"""

import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
import numpy as np

Xb, yb = mglearn.datasets.load_extended_boston()
Xb_train, Xb_test, yb_train, yb_test = train_test_split(Xb, yb, random_state = 0)
lasso = Lasso().fit(Xb_train, yb_train)

print("Boston training set score")
print(lasso.score(Xb_train, yb_train))  
print("Boston test set score")
print(lasso.score(Xb_test, yb_test))
print("Number of features used:")
print(np.sum(lasso.coef_ != 0))

#try reducing undertfitting by decreasing alpha (also need to
#increase number of iterations)

lasso001 = Lasso(alpha=0.0001, max_iter=100000).fit(Xb_train, yb_train)
print("Boston001 training set score")
print(lasso001.score(Xb_train, yb_train))  
print("Boston001 test set score")
print(lasso001.score(Xb_test, yb_test))
print("Number of features used:")
print(np.sum(lasso001.coef_ != 0))