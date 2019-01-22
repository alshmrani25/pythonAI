#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:42:28 2018

@author: djesse
"""

from search_classes import GraphProblem
from search_classes import EightPuzzleProblem
from search_functions import astar_search
from search_functions import get_solution_path
  
wGraph = GraphProblem("romania_map.txt", "Arad", "Bucharest")
#print(wGraph)
solutionNode = astar_search(wGraph)
#print("solution node")
#print(solutionNode)
print("solution path")
print(get_solution_path(solutionNode))

startEight = ((7,2,4),(5,0,6),(8,3,1))
goalEight = ((0,1,2),(3,4,5),(6,7,8))

eightProb = EightPuzzleProblem(startEight, goalEight)
print("eight problem")
print(eightProb)
eightSolutionNode = astar_search(eightProb)
print("solution node")
print(eightSolutionNode )
print("solution path")
print(get_solution_path(eightSolutionNode ))
