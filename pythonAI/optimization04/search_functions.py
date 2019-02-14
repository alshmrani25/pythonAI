# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:01:44 2018

@author: domje
"""

import random
import math

def simulated_annealing_search(problem, schedule):
    currentNode = problem.initial_node
    for key, value in schedule.items():
        temp = value
        if temp == 0:
            return currentNode
        #randomly grab a next node
        allSuccessorNodes = problem.get_successors(currentNode)
        nextNode = random.choice(allSuccessorNodes)
        changeInValue = problem.get_heuristic_value(nextNode.state) - problem.get_heuristic_value(currentNode.state)
        if changeInValue > 0:
            currentNode = nextNode
        else:
            changeProbability = math.exp(changeInValue / temp)
            if random.random() < changeProbability:
                currentNode = nextNode
    
#population is a set of tuples (careful), but needs to return list
def genetic_algorithm(problem, population, max_iterations = 250000):
    for count in range(1, max_iterations):
        new_population = set() 
        for i in range(1, len(population) + 1):
            fitness_map = fitness_function(problem, population)
            #prevent identical parents
            x = []
            y = []
            while sorted(x) == sorted(y) or len(x) < 1 or len(y) < 1:
                x = random_fitness_selection(fitness_map)
                y = random_fitness_selection(fitness_map)
            #added this to prevent identical children (which can't
            #be added to the set)
            child = []
            while len(child) < 1 or tuple(child) in new_population:
                child = reproduce(x, y)
                if random.random() < 0.05:
                    child = mutate(child)
            new_population.add(tuple(child))
        population = new_population
    #now return the best individual in the final population
    final_fitness_map = fitness_function(problem, population)
    return get_highest_fitness(final_fitness_map)

#assumes states are 1D lists
#returns map of fitnesses, where lists are tuples for Python reasons
def fitness_function(problem, population):
    sumHeuristic = 0
    for state in population:
        sumHeuristic = sumHeuristic + problem.get_heuristic_value(list(state))
    fitnessMap = {}
    for state in population:
        fitnessMap[state] = problem.get_heuristic_value(list(state)) / sumHeuristic
    return fitnessMap

#assumes keys of tuples mapped to probabilities which all add to 1.0
def random_fitness_selection(fitnessMap):
    #now randomly grab one of map items, based on the probability
    #careful to return a list from a tuple
    randomProbability = random.random()
    currentProbabilityStatus = 0
    for key, value in fitnessMap.items():
        currentProbabilityStatus = currentProbabilityStatus + value
        if randomProbability < currentProbabilityStatus:
            return list(key)

def get_highest_fitness(fitnessMap):
    bestProbability = 0
    bestTuple = None
    for key, value in fitnessMap.items():
        if value > bestProbability:
            bestProbability = value
            bestTuple = key
    return list(bestTuple)

#assumes input is 1D lists        
def reproduce(x, y):
    length = len(x)
    randIndex = random.randrange(1, length)
    child = x[0 : randIndex] + y[randIndex : length]
    return child

#defaults to 8Queen settings; assumes 1D list
def mutate(x, minValue = 1, maxValue = 8, randIncrement = 1):
    randIndex = random.randrange(1, len(x))
    randReplace = None
    while randReplace == x[randIndex] or randReplace == None:
        randReplace = random.randrange(minValue, maxValue, randIncrement)
    x[randIndex] = randReplace
    return x
    


#helper function to get a temperature map for simulated annealing
#this isn't optimal, but using this method
def get_temperature_schedule():
    schedule = {}
    maxTemp = 1000;
    maxTime = 100000
    for time in range(1, maxTime, 1):
        schedule[time] = maxTemp = maxTemp * 0.99
    schedule[maxTime] = 0
    return schedule



def and_or_graph_search(problem):
    return or_search(problem.initial_state, problem, [])

def or_search(state, problem, path):
    return 0

def and_search(state, problem, path):
    return 0




if __name__ == "__main__":
    print("This is a module for optimization functions.")
    input("\n\nPlease press Enter to exit.")