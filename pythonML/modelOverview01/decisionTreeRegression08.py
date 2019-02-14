# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:46:51 2019

@author: domje

DON'T USE DECISION TREE FOR REGRESSION - for reasons this code illustrates.

Compare Decision Tree regression to Linear Regression

Here, the Decision Tree prediction (post-2000) is messed 
up because Tree models CANNOT GENERATE NEW RESPONSES
OUTSIDE WHAT THE TRAINING DATA USES!!!

It is _theoretically_ possible to use decision tree regression for some
limited situations according to the book, such as if a price will go up or down.


"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Moore's law illustrated....
ram_prices = pd.read_csv("ram_price.csv")
#plt.semilogy(ram_prices.date, ram_prices.price)
#plt.xlabel("Year")
#plt.ylabel("Price in $/MB")

data_train = ram_prices[ram_prices.date < 2000]
data_test = ram_prices[ram_prices.date >= 2000]
X_train = data_train.date[:, np.newaxis]
#note the use of logorithmic transformation
#they say it will simplify things
y_train = np.log(data_train.price)

tree = DecisionTreeRegressor().fit(X_train, y_train)
linear_reg = LinearRegression().fit(X_train, y_train)

X_all = ram_prices.date[:, np.newaxis]

pred_tree = tree.predict(X_all)
pred_lr = linear_reg.predict(X_all)

#undo logiritmic transformation
price_tree = np.exp(pred_tree)
price_lr = np.exp(pred_lr)

plt.semilogy(data_train.date, data_train.price, label="Training Data")
plt.semilogy(data_test.date, data_test.price, label="Testing Data")
plt.semilogy(ram_prices.date, price_tree, label="Tree Prediction")
plt.semilogy(ram_prices.date, price_lr, label="Linear Prediction")
plt.legend()
