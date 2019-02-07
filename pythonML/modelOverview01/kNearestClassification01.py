#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:16:04 2018

@author: djesse

Chapter 2 of the book; evaluates dfferent models

p. 32

K Nearest Neighbors, Classification

-NOT USED IN PRACTICE
- simple because it only stores data
- parameters = n of neighbors and manner of distance measurement (Euclidean is fine)
    - the larger n is, the simpler the model, and vice versa
- usually a good model to try first
- usually need to preprocess data
- bad with models with 100s of features; worse when those features hold many 0s

"""

import mglearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

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


#cancer data
cancer = load_breast_cancer()
#print("Keys ", cancer.keys())
#print("Shape ", cancer.data.shape)
#print("Sample counts per class ")
count_by_class = { n: v for n, v in zip(cancer.target_names
    , np.bincount(cancer.target)) }
#print(count_by_class)
#print("Feature names ", cancer.feature_names)
#print(cancer.DESCR)

Xc_train, Xc_test, yc_train, yc_test = train_test_split(cancer.data
    , cancer.target, stratify=cancer.target, random_state=66)
training_accuracy = []
test_accuracy = []
k_neighbor_values = range(1,11)

for k in k_neighbor_values:
    #build model
    clfc = KNeighborsClassifier(n_neighbors = k)
    clfc.fit(Xc_train, yc_train)
    #record training accuracy (for academic reasons)
    training_accuracy.append(clfc.score(Xc_train, yc_train))
    #record test accuracy
    test_accuracy.append(clfc.score(Xc_test, yc_test))
    
plt.plot(k_neighbor_values, training_accuracy, label="Training Accuracy")
plt.plot(k_neighbor_values, test_accuracy, label="Test Accuracy")
plt.ylabel("Accuracy %")
plt.xlabel("N neighbors")
plt.legend()