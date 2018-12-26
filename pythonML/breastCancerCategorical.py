#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:27:13 2018

@author: djesse
"""

from sklearn.datasets import load_breast_cancer
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

cancer = load_breast_cancer()
#print("Keys ", cancer.keys())
#print("Shape ", cancer.data.shape)
#print("Sample counts per class ")
count_by_class = { n: v for n, v in zip(cancer.target_names
    , np.bincount(cancer.target)) }
#print(count_by_class)
#print("Feature names ", cancer.feature_names)
#print(cancer.DESCR)

X_train, X_test, y_train, y_test = train_test_split(cancer.data
    , cancer.target, stratify=cancer.target, random_state=66)
training_accuracy = []
test_accuracy = []
k_neighbor_values = range(1,11)

for k in k_neighbor_values:
    #build model
    clf = KNeighborsClassifier(n_neighbors = k)
    clf.fit(X_train, y_train)
    #record training accuracy (for academic reasons)
    training_accuracy.append(clf.score(X_train, y_train))
    #record test accuracy
    test_accuracy.append(clf.score(X_test, y_test))
    
plt.plot(k_neighbor_values, training_accuracy, label="Training Accuracy")
plt.plot(k_neighbor_values, test_accuracy, label="Test Accuracy")
plt.ylabel("Accuracy %")
plt.xlabel("N neighbors")
plt.legend()