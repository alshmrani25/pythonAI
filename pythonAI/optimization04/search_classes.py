#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:41:43 2018

@author: djesse
"""


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
        if parent:
            self.depth = parent.depth + 1
            self.state = problem.get_result(parent.state, action)
            self.path_cost = parent.path_cost + problem.get_step_cost(parent.state, action)
            self.action = action
        else:
            self.state = action
            self.action = None
            
    def __str__ (self):
        rep = "<Node\n"
        rep += "\t State: " + str(self.state) + "\n"
        rep += "\tPath Cost: " + str(self.path_cost) + "\n"
        rep += "\tParent: " + str(self.parent.state) if self.parent else "" + "\n"
        rep += "\tAction: " + str(self.action) if self.action else "" + "\n"
        rep += ">"
        return rep

    #needed for comparisons
    def __lt__(self, other):
        return self.path_cost < other.path_cost
    
    def get_child_node(self, problem, action):
        return Node(problem, self, action)
    
    
    
class EightQueensProblem(object):    
    '''
    Represents a chessboard where you need to place 8 queens
    where none of them can attack the other
    STATE - since we know there can only be one
    queen in each column, an 8-digit numbers will hold
    the state (each one represents columns a-h, and the row, with
    row 1 facing the white player)
    '''
    initial_state = None
    initial_node = None
    heuristic_value = None
    
    def __init__(self):
        #the initial state is a setup where each column has a queen
        #placed in a random row; use a random placement of 1-8
        
        
        
        
        self.initial_state = random_initial_state
        self.initial_node = Node(self, None, initial_state)
        
    def __str__(self):
        rep = "<EightQueensProblem\n"
        rep += "\tInitial State: " + str(self.initial_state) + "\n>"
        return rep
    
    def expand_node(self, nodeState):
        new_actions = []
        
        return new_actions
    
    def get_result(self, state, action):
        return None
    
    def goal_test(self, state):
        #0 means no queens are attacking each other
        if self.get_heuristic_value == 0:
            return True
        return False

    def get_step_cost(self, state, action):
        #action = the next state; should always be 1
        if action:
            return 1
        else:
            return 0
    
    def get_heuristic_value(self, node):
        #For this problem, the number of "attacks" possible between queens
        total = 0
        
        
        return total
   
    
if __name__ == "__main__":
    print("This is a module for optimization classes.")
    input("\n\nPlease press Enter to exit.")