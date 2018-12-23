#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:16:04 2018

@author: djesse

Chapter 2 of the book; evaluates dfferent models

"""

import mglearn
import matplotlib.pyplot as plt

#forge dataset, 2-class classification
X, y = mglearn.datasets.make_forge()
#plot
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First Feature")
plt.ylabel("Second Feature")
print(X.shape)
