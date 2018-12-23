#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:42:28 2018

@author: djesse
"""

from search_classes import WeightedGraphProblem


wGraph = WeightedGraphProblem("romania_map.txt", "Arad", "Bucharest")
print(wGraph)
nodesBucharest = wGraph.expandNode("Bucharest")

for node in nodesBucharest:
    print(node)