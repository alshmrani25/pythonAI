# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:01:44 2018

@author: domje
"""

import random
import math

def simulated_annealing_search(problem, schedule):
    currentNode = problem.initial_node
    for time in range (1, 2001, 1):
        temp = schedule[time]
        if temp == 0:
            return currentNode
        #randomly grab a next node
        allSuccessorNodes = problem.get_successors(currentNode)
        nextNode = random.choice(allSuccessorNodes)
        changeInValue =  problem.get_heuristic_value(nextNode) - problem.get_heuristic_value(currentNode)
        if changeInValue > 0:
            currentNode = nextNode
        else:
            changeProbability = math.exp(changeInValue / temp)
            if random.random() < changeProbability:
                currentNode = nextNode
    

def genetic_search(problem):
    return problem


#helper function to get a temperature map for simulated annealing
#this isn't optimal, but...
def get_temperature_schedule():
    schedule = {}
    for time in range(1, 2001, 1):
        schedule[time] = 500 - (time / 4)
    return schedule

if __name__ == "__main__":
    print("This is a module for optimization functions.")
    input("\n\nPlease press Enter to exit.")