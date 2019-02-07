# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:20:18 2019

@author: domje

Linear Classification models

- best for binary classification (except Logistic regression)
- parameter = C
    - the higher, the less regulatization
- better for higher dimensions
- very fast and good for large data sets
- good for sparse data and large # of features compared to samples
- hard to understand coefficients
- sometimes only feasible method for really large data sets

"""

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import mglearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = mglearn.datasets.make_forge()
fig, axes = plt.subplots(1, 2, figsize=(10,3))

for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
    clf = model.fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5, ax=ax, alpha=.7)
    mglearn.discrete_scatter(X[:, 0], X[:,1], y, ax=ax)
    ax.set_title(clf.__class__.__name__)
    ax.set_xlabel("Feature 0")
    ax.set_ylabel("Feature 1")  

axes[0].legend()

#cancer test
cancer = load_breast_cancer()
Xc_train, Xc_test, yc_train, yc_test = train_test_split(cancer.data
    , cancer.target, stratify=cancer.target, random_state=42)
logreg = LogisticRegression().fit(Xc_train, yc_train)
print("Cancer training set score: ", logreg.score(Xc_train, yc_train))
print("Cancer testing set score: ", logreg.score(Xc_test, yc_test))

logreg001 = LogisticRegression(C=0.01).fit(Xc_train, yc_train)
print("Cancer training 0.01 set score: ", logreg001.score(Xc_train, yc_train))
print("Cancer testing 0.01 set score: ", logreg001.score(Xc_test, yc_test))
