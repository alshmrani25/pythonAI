#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:42:28 2018

@author: djesse
"""

from search_classes import EightQueensProblem
from search_functions import simulated_annealing_search
from search_functions import genetic_search
from search_functions import get_temperature_schedule

tSchedule = get_temperature_schedule()

qGraph = EightQueensProblem()
solutionNode = simulated_annealing_search(qGraph, tSchedule)
print("annealing solution node")
print(solutionNode)
print(qGraph.get_heuristic_value(solutionNode))

#solutionNode2 = genetic_search(qGraph)
#print("genetic solution node")
#print(solutionNode2)
