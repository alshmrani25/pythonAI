#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:27:13 2018

@author: djesse
"""

from sklearn.datasets import load_breast_cancer
import numpy as np

cancer = load_breast_cancer()
print("Keys ", cancer.keys())
print("Shape ", cancer.data.shape)
print("Sample counts per class ")
count_by_class = { n: v for n, v in zip(cancer.target_names
    , np.bincount(cancer.target)) }
print(count_by_class)
print("Feature names ", cancer.feature_names)
print(cancer.DESCR)