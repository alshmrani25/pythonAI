#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:42:28 2018

@author: djesse
"""

from search_classes import EightQueensProblem
from search_functions import simulated_annealing_search
from search_functions import genetic_algorithm
from search_functions import get_temperature_schedule
from search_functions import genetic_algorithm

"""
tSchedule = get_temperature_schedule()

qGraph = EightQueensProblem()
solutionNode = simulated_annealing_search(qGraph, tSchedule)
print("annealing solution node")
print(solutionNode)
print(qGraph.get_heuristic_value(solutionNode.state))
"""

genGraph = EightQueensProblem()
genPop = set()
genPop.add((1,2,3,4,5,6,7,8))
genPop.add((1,3,5,7,2,3,6,8))
genPop.add((8,7,6,5,4,3,2,1))
genPop.add((8,6,4,2,7,5,3,1))
genList = genetic_algorithm(genGraph, genPop)
print(genList)



#solutionNode2 = genetic_search(qGraph)
#print("genetic solution node")
#print(solutionNode2)
