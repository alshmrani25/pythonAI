#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:16:04 2018

@author: djesse

Chapter 2 of the book; evaluates dfferent models

"""

import mglearn
import matplotlib.pyplot as plt

#wave dataset, to demonstrate regression
X,y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel("Feature")
plt.ylabel("Target")