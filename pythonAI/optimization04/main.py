#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:42:28 2018

@author: djesse
"""

from search_classes import EightQueensProblem
from search_methods import simulated_annealing_search
from search_methods import genetic_search

qGraph = EightQueensProblem()
print(qGraph)
solutionNode = simulated_annealing_search(qGraph)
print("annealing solution node")
print(solutionNode)
solutionNode2 = genetic_search(qGraph)
print("genetic solution node")
print(solutionNode2)
