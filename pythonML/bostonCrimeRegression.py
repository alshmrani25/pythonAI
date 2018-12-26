#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:44:13 2018

@author: djesse
"""

from sklearn.datasets import load_boston
import mglearn

boston = load_boston()
print("Shape: " , boston.data.shape)
X, y = mglearn.datasets.load_extended_boston()
print(X.shape)