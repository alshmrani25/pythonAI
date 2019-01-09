#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:42:28 2018

@author: djesse
"""

from search_classes import GraphProblem
from search_methods import astar_search
from search_methods import get_solution_path

wGraph = GraphProblem("romania_map.txt", "Arad", "Bucharest")
print(wGraph)
solutionNode = astar_search(wGraph)
print("solution node")
print(solutionNode)
print("solution path")
print(get_solution_path(solutionNode))