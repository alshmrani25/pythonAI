#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:16:04 2018

@author: djesse

Chapter 2 of the book; evaluates dfferent models

"""

import mglearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#forge dataset, 2-class classification
X, y = mglearn.datasets.make_forge()
#plot
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First Feature")
plt.ylabel("Second Feature")
print(X.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#mglearn.plots.plot_knn_classification(n_neighbors=1)
#mglearn.plots.plot_knn_classification(n_neighbors=3)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
print("Predictions: ", clf.predict(X_test))
print("Accuracy: " , clf.score(X_test, y_test))