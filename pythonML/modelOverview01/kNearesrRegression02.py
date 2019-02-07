#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:16:04 2018

@author: djesse

Chapter 2 of the book; evaluates dfferent models

p. 33

K Nearest Neighbors, Regression




"""

import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

#wave dataset, to demonstrate regression
X,y = mglearn.datasets.make_wave(n_samples=40)
#mglearn.plots.plot_knn_regression(n_neighbors=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

fig, axes = plt.subplots(1,3,figsize=(15,4))
#create 1000 data points, evenly spaced between -3 and 3
line = np.linspace(-3, 3, 1000).reshape(-1, 1)
for n, ax in zip([1,3,9], axes):
    #make a prediction with 1,3,or 9 n
    reg = KNeighborsRegressor(n_neighbors = n)
    reg.fit(X_train, y_train)
    ax.plot(line, reg.predict(line))
    ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
    ax.plot(X_test, y_test, '^', c=mglearn.cm2(1), markersize=8)
    ax.set_title(str(n) + " Neightbors, Test Score: " + str(reg.score(X_test, y_test)))
    ax.set_xlabel("Feature")
    ax.set_ylabel("Target")
    axes[0].legend(["Model Prediction", "Training Data/Target", "Test Data/Target"], loc="best")
    

#boston data
from sklearn.datasets import load_boston

boston = load_boston()
print("Shape: " , boston.data.shape)
Xc, yc = mglearn.datasets.load_extended_boston()
print(Xc.shape)