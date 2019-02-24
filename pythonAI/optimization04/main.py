#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:42:28 2018

@author: djesse
"""

from search_classes import EightQueensProblem
from search_classes import VacuumWorldErratic
from search_functions import simulated_annealing_search
from search_functions import get_temperature_schedule
from search_functions import genetic_algorithm
from search_functions import and_or_graph_search


tSchedule = get_temperature_schedule()

qGraph = EightQueensProblem()
solutionNode = simulated_annealing_search(qGraph, tSchedule)
print("annealing solution node")
print(solutionNode)
print(qGraph.get_heuristic_value(solutionNode.state))



#This takes 500x the time of simulated annealing, and only gets a solution
#90%-95% as good!!!
"""
genGraph = EightQueensProblem()
genPop = set()
genPop.add((2,4,7,4,8,5,5,2))
genPop.add((3,2,7,5,2,4,1,1))
genPop.add((2,4,4,1,5,1,2,4))
genPop.add((3,2,5,4,3,2,1,3))
genList = genetic_algorithm(genGraph, genPop)
print("genetic algorithm solution")
print(genList)
print(genGraph.get_heuristic_value(genList))
"""

vWorld = VacuumWorldErratic()
solutionPath = and_or_graph_search(vWorld)
print("final solution", solutionPath)