# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:40:36 2019

@author: domje

Tree where leaves are the answers.
Rather than binary questions, usually asks if "i > a"?
Partitions the training data (think squares on 2D data) to get minimal depth tree.

Main problem - overfitting. Uses pruning to avoid that (pre or post).
Some paras are max tree depth and max num of points in node to keep splitting it.
This causes train/test accuracy tradeoff.
NOTE - skikit-learn ONLY implements pre-pruning

NOTE - using GraphViz app to view .DOT files




"""



from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

def plot_feature_importances(model, data_set):
    n_features = data_set.data.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), data_set.feature_names)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)

cancer = load_breast_cancer()
Xc_train, Xc_test, yc_train, yc_test = train_test_split(cancer.data
    , cancer.target, stratify=cancer.target, random_state=42)
tree = DecisionTreeClassifier(random_state = 0)
tree.fit(Xc_train, yc_train)
print("Training set accuracy: ", tree.score(Xc_train, yc_train))
print("Test set accuracy: ", tree.score(Xc_test, yc_test))   

tree2 = DecisionTreeClassifier(max_depth = 4, random_state = 0)
tree2.fit(Xc_train, yc_train)
print("Training set accuracy, max depth set: ", tree2.score(Xc_train, yc_train))
print("Test set accuracy, max depth set: ", tree2.score(Xc_test, yc_test))

#create .dot file based on this data
#export_graphviz(tree2, out_file="tree2.dot", class_names=["malignant", "benign"]
#    , feature_names = cancer.feature_names, impurity=False, filled=True)

#the below is hard to read
print(cancer.feature_names)
print("Feature importance: \n", tree2.feature_importances_)
#this is better - graphs out which features of data are being used in branching
plot_feature_importances(tree2, cancer)