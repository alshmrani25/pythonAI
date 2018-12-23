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
    NOTE - all problems must have methods (Python doesn't have true interfaces
        , and these methods will differ drastically by problem)
    - get_state_result(parent_state, action)
    - get_path_cost(parent_state, action)
    '''
    state = None
    parent = None
    action = None
    path_cost = 0
    def __init__(self, problem, parent, action):
        self.state = problem.get_state_result(parent.state, action)
        self.parent = parent
        self.action = action
        self.path_cost = self.get_path_cost(problem, parent, action)
    def get_path_cost(self, problem, parent, action):
            self.path_cost = parent.path_cost + problem.get_path_cost(parent.state, action)


class WeightedGraphEdge(object):
    '''Represents data input - the space between two points (in a weighted graph)'''
    endpoints = []
    weight = 0
    def __init__(self, endpointA, endpointB, wt):
        self.endpoints = [endpointA, endpointB]
        self.weight = wt
    def __str__(self):
        rep = "<WeightedGraphEdge, " + self.endpoints[0] + "-" + self.endpoints[1] + ": " + str(self.weight) + ">"
        rep = rep.replace("\n", "") #keep it on one line
        return rep

class WeightedGraphProblem(object):
    '''
    Represents a graph of weighted nodes.
    
    Imports a text file into a weighted graph.
    Text file must be of format, for each line:
    LOCA_String, LOCB_String, distance_number
    '''
    initial_state = None
    goal_state = None
    frontier_fifo = Queue()
    explored_set = set()
    node_list = []
    def __init__(self, file_name, initial_state, goal_state):
        data_file = open(file_name, "r")
        lines = data_file.readlines()
        self.initial_state = initial_state
        self.goal_state = goal_state
        for line in lines:
            line_data = line.split(",")
            self.node_list.append(WeightedGraphEdge(line_data[0].strip(), line_data[1].strip(), line_data[2]))
    def __str__(self):
        rep = "<WeightedGraphProblem\n"
        rep += "\tInitial State: " + self.initial_state + "\n"
        rep += "\tGoal State: " + self.goal_state + "\n"
        for node in self.node_list:
            rep += "\t" + str(node) + "\n"
        rep += "\n>"
        return rep
    def getConnectedPoints(self, nodeName):
        nodes = []
        for node in self.node_list:
            if nodeName in node.endpoints:
                nodes.append(node)
        return nodes
    def get_state_result(self, parent_state, action):
        #the action here will be the name of the city traveled to
        if not parent_state:
            return self.initial_state
        else:
            
    def get_path_cost(self, parent_state, action):
        travel_edges = self.getConnectedPoints(parent_state)
        for edge in travel_edges:
            if parent_state in edge.endpoints and action in edge.endpoints:
                return edge.weight
        return None
    def breadth_first_search(self):
        initial_node = Node(self, None, None)
    
        while True:
            if self.frontier_fifo.empty():
                return False
            node = self.frontier_fifo.get()
            self.explored_set.add(node.state)
            
            
    
    def a_star_search(self):
        return 0
            
    
if __name__ == "__main__":
    print("This is a module for searching classes.")
    input("\n\nPlease press Enter to exit.")