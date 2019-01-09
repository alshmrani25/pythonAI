#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:41:43 2018

@author: djesse
"""

from queue import Queue

class Node(object):
    '''
    Represents generic node in a solution graph, created by the problem.
    '''   
    state = None
    parent = None
    action = None
    path_cost = 0
    depth = 0
    
    def __init__(self, problem, parent = None, action = None):
        self.parent = parent
        self.action = action
        if parent:
            self.depth = parent.depth + 1
            self.state = problem.get_result(parent.state, action)
            self.path_cost = parent.path_cost + problem.get_step_cost(parent.state, action)
        else:
            self.state = action
            
    def __str__ (self):
        rep = "<Node\n"
        rep += "\t State: " + self.state + "\n"
        rep += "\tPath Cost: " + str(self.path_cost) + "\n"
        rep += "\tParent: " + self.parent.state if self.parent else "" + "\n"
        rep += ">"
        return rep
    
    def get_child_node(self, problem, action):
        return Node(problem, self, action)

class GraphProblem(object):
    '''
    Represents a graph of weighted nodes.
    
    Imports a text file into a weighted graph.
    Text file must be of format, for each line:
    LOCA_String, LOCB_String, distance_number
    '''
    data_lines = None #holds the raw data from the text file
    initial_state = None
    initial_node = None
    goal_state = None
    
    def __init__(self, file_name, initial_state, goal_state):
        data_file = open(file_name, "r")
        self.data_lines = data_file.readlines()
        self.goal_state = goal_state
        self.initial_state = initial_state
        self.initial_node = Node(self, None, initial_state)
        
    def __str__(self):
        rep = "<WeightedGraphProblem\n"
        rep += "\tInitial State: " + self.initial_state + "\n"
        rep += "\tGoal State: " + self.goal_state + "\n>"
        return rep
    
    #helper function
    def find_edge(self, from_state, to_state):
        for line in self.data_lines:
            locs = set()
            line = line.replace("\n", "")
            line_data = line.split(",")
            locs.add(line_data[0].strip())
            locs.add(line_data[1].strip())
            if from_state in locs and to_state in locs:
                return line_data
        return None    
        
    def expand_node(self, nodeState):
        new_states = []
        for line in self.data_lines:
            locs = set()
            line_data = line.split(",")
            locs.add(line_data[0].strip())
            locs.add(line_data[1].strip())
            if nodeState == line_data[0].strip():
                new_states.append(line_data[1].strip())
            elif nodeState == line_data[1].strip():
                new_states.append(line_data[0].strip())
        return new_states
    
    def get_result(self, state, action):
        #the action here will be the name of the city traveled to
        if not state:
            return self.initial_state
        elif self.find_edge(state, action):
            return action
        else:
            return None
    
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        return False
    
    def get_step_cost(self, state, action):
        #the state is the name of the city traveled from 
        #the action here will be the name of the city traveled to
        if action == self.initial_state:
            return 0
        else:
            line_data = self.find_edge(state, action)
            if line_data:
                return float(line_data[2])

        return 0
    
    def get_astar_heuristic_cost(self, node):
        #you would usually use a standard distance equation here,
        #but that's not available in the dataset provided
        return 0
    
if __name__ == "__main__":
    print("This is a module for searching classes.")
    input("\n\nPlease press Enter to exit.")