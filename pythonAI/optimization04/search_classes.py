#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:41:43 2018

@author: djesse


"""

from random import shuffle
from random import randrange


class Node(object):
    '''
    Represents generic node in a solution graph, created by the problem.
    '''   
    state = None
    parent = None
    path_cost = 0
    
    def __init__(self, problem, state, parent = None):
        
        if parent:
            self.state = state
            self.path_cost = parent.path_cost + problem.get_step_cost()
        else:
            self.state = state
            self.path_cost = 0
            
    def __str__ (self):
        rep = "<Node\n"
        rep += "\t State: " + str(self.state) + "\n"
        rep += "\tPath Cost: " + str(self.path_cost) + "\n"
        rep += ">"
        return rep

    #needed for comparisons
    def __lt__(self, other):
        return self.path_cost < other.path_cost
    
    
    
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
        random_initial_state = [1,2,3,4,5,6,7,8]
        shuffle(random_initial_state)
        
        self.initial_state = random_initial_state
        self.initial_node = Node(self, self.initial_state, None)
        
    def __str__(self):
        rep = "<EightQueensProblem\n"
        rep += "\tInitial State: " + str(self.initial_state) + "\n>"
        return rep
    
    def get_successors(self, node):
        successor_nodes = []
        for index, value in enumerate(node.state):
            for newValue in range(1, len(node.state) + 1, 1):
                if newValue != value:
                    newState = node.state.copy()
                    newState[index] = newValue
                    newNode = Node(self, newState, node)
                    successor_nodes.append(newNode)
        
        return successor_nodes
    
    def goal_test(self, node):
        #100 means no queens are attacking each other
        if self.get_heuristic_value(node.state) == 100:
            return True
        return False

    def get_step_cost(self):
        return 1
    
    def get_heuristic_value(self, nodeState):
        #For this problem, the number of "attacks" possible between queens
        total = 0
        for index, value in enumerate(nodeState):
            foundLeftRowHit = False
            foundLeftUpDiagHit = False
            foundLeftDownDiagHit = False
            foundRightRowHit = False
            foundRightUpDiagHit = False
            foundRightDownDiagHit = False
            leftUpDiag = value
            leftDownDiag = value
            rightUpDiag = value
            rightDownDiag = value
            for leftIndex in range(index - 1, -1, -1):
                leftUpDiag = leftUpDiag + 1
                leftDownDiag = leftDownDiag - 1
                if value == nodeState[leftIndex]:
                    foundLeftRowHit = True
                if leftUpDiag == nodeState[leftIndex]:
                    foundLeftUpDiagHit = True
                if leftDownDiag == nodeState[leftIndex]:
                    foundLeftDownDiagHit = True
            for rightIndex in range(index + 1, len(nodeState), 1):    
                rightUpDiag = rightUpDiag + 1
                rightDownDiag = rightDownDiag - 1
                if value == nodeState[rightIndex]:
                    foundRightRowHit = True
                if rightUpDiag == nodeState[rightIndex]:
                    foundRightUpDiagHit = True
                if rightDownDiag == nodeState[rightIndex]:
                    foundRightDownDiagHit = True
            if foundLeftRowHit:
                total = total + 1
            if foundLeftUpDiagHit:
                total = total + 1
            if foundLeftDownDiagHit:
                total = total + 1
            if foundRightRowHit:
                total = total + 1
            if foundRightUpDiagHit:
                total = total + 1
            if foundRightDownDiagHit:
                total = total + 1
        
        #need to return a "maximizing" heuristic
        return 100 - total
   
    
class VacuumWorldErratic(object):
    '''
    Represents a 2-space world occupied by a vacuum cleaner, and
    possible dirt. This erratic varation means:
        1. Suck action on dirty square cleans the current square and SOMETIMES the other square too.
        2. Suck action on a clean square SOMETIMES drops dirt on carpet.
    '''
    initial_state = None
    #initial_node = None
    heuristic_value = None
    
    def __init__(self):
        #there are 8 possible states - see p. 134, Figure 4.9
        #self.initial_state = randrange(1,8)
        self.initial_state = 1
        #self.initial_node = Node(self, self.initial_state, None)
        
    def __str__(self):
        rep = "<VacuumWorldErratic\n"
        rep += "\tInitial State: " + str(self.initial_state) + "\n>"
        return rep
    
    def get_actions(self, nodeState):
        #return set of possible actions
        state_actions = {
            1: set(["Suck", "Right"])
            , 2: set(["Suck", "Left"])
            , 3: set(["Suck", "Right"])
            , 4: set(["Suck", "Left"])
            , 5: set(["Suck", "Right"])
            , 6: set(["Suck", "Left"])
            , 7: set(["Suck", "Right"])
            , 8: set(["Suck", "Left"])
        }
        return state_actions[nodeState]
    
    def get_results(self, nodeState, action):
        #this will return a set of POSSIBLE state results
        #actions = Left, Right, Suck
        state_results = {
                1: { "Left": set([1]), "Right": set([2]), "Suck": set([5, 7])  }
                , 2: { "Left": set([1]), "Right": set([2]), "Suck": set([4, 8])  }
                , 3: { "Left": set([3]), "Right": set([4]), "Suck": set([7])  }
                , 4: { "Left": set([3]), "Right": set([4]), "Suck": set([4, 2])  }
                , 5: { "Left": set([5]), "Right": set([6]), "Suck": set([5, 1])  }
                , 6: { "Left": set([5]), "Right": set([6]), "Suck": set([8])  }
                , 7: { "Left": set([7]), "Right": set([8]), "Suck": set([7, 3])  }
                , 8: { "Left": set([7]), "Right": set([8]), "Suck": set([8, 6])  }
                }
        return state_results[nodeState][action]
        
    
    def goal_test(self, nodeState):
        #if all squares are clean, you're done
        if self.get_heuristic_value(nodeState) == 0:
            return True
        return False

    def get_step_cost(self):
        return 1
    
    def get_heuristic_value(self, nodeState):
        #For this problem, the number of dirts left
        if nodeState < 3:
            return 2
        elif nodeState >= 3 and nodeState < 7:
            return 1
        else:
            return 0
    
class VacuumWorldNoObservation(object):
    '''
    Represents a 2-space world occupied by a vacuum cleaner, and
    possible dirt. This no observation varation means:
        1. Vacuum knows the "geography" of the world
        2. Vaccum doesn't know the location of any dirt
        3. THEREFORE doesn't know its precise state
    So, the vacuum uses a "belief state" to guess at
    which state it's in.
    This is for the DETERMINISTIC problem, but approach would work
    for both deterministic and non-deterministic problems.
    '''
    belief_states = set([1,2,3,4,5,6,7,8])
    heuristic_value = None
    
    
    def __init__(self):
        #there are 8 possible states - see p. 134, Figure 4.9
        self.initial_state = self.belief_states
        
    def __str__(self):
        rep = "<VacuumWorldNoObservation\n"
        rep += "\tBelief States: " + str(self.belief_states) + "\n>"
        return rep
    
    def get_actions(self, nodeStateSet):
        #return set of possible actions
        
        if type(nodeStateSet) is int:
            nodeStateSet = set([nodeStateSet])
        
        state_actions = {
            1: set(["Suck", "Right"])
            , 2: set(["Suck", "Left"])
            , 3: set(["Suck", "Right"])
            , 4: set(["Suck", "Left"])
            , 5: set(["Suck", "Right"])
            , 6: set(["Suck", "Left"])
            , 7: set(["Suck", "Right"])
            , 8: set(["Suck", "Left"])
        }
        
        actionsFinal = set()
        for state in nodeStateSet:
            actionSet = state_actions[state]
            for action in actionSet:
                actionsFinal.add(action)
        
        return actionsFinal
    
    def get_results(self, nodeStateSet, action):
        #NOTE - the nodeState fed in will be the SELF.belief_states
        #this will return a set of POSSIBLE state results
        #n^2 possibilities!!!!! WILL HAVE TO HAVE PARTIAL LIST BASED
        #ON REACHABLE SETS FROM THE BEGINNING (branch down...)
        #actions = Left, Right, Suck
        #key = tuple (representing belief state)
        
        if type(nodeStateSet) is int:
            nodeStateTuple = (nodeStateSet,)
        else:
            nodeStateTuple = tuple(nodeStateSet)
        
        action_results = {
                (1,2,3,4,5,6,7,8): { "Left": set([1,3,5,7]), "Right": set([2,4,6,8]), "Suck": set([1,3,4,8])  }
                , (1,3,4,8): { "Left": set([1,3,7]), "Right": set([2,4,8]), "Suck": set([4,5,7,8])  }
                , (4,5,7,8): { "Left": set([3,5,7]), "Right": set([4,6,8]), "Suck": set([4,5,7,8])  }
                , (1,3,7): { "Left": set([1,3,7]), "Right": set([2,4,8]), "Suck": set([5,7])  }
                , (2,4,8): { "Left": set([1,4,7]), "Right": set([2,4,8]), "Suck": set([4,8])  }
                , (1,3,5,7): { "Left": set([1,3,5,7]), "Right": set([2,4,6,8]), "Suck": set([5,7])  }
                , (2,4,6,8): { "Left": set([1,3,5,7]), "Right": set([2,4,6,8]), "Suck": set([4,8])  }
                , (5,7): { "Left": set([5,7]), "Right": set([6,8]), "Suck": set([5,7])  }
                , (4,8): { "Left": set([3,7]), "Right": set([4,8]), "Suck": set([4,8])  }
                , (6,8): { "Left": set([5,7]), "Right": set([6,8]), "Suck": set([8])  }
                , (3,7): { "Left": set([3,7]), "Right": set([4,8]), "Suck": set([7])  }
                , (1,):  { "Left": set([1]), "Right": set([2]), "Suck": set([5])  }
                , (2,):  { "Left": set([1]), "Right": set([2]), "Suck": set([4])  }
                , (3,):  { "Left": set([3]), "Right": set([4]), "Suck": set([7])  }
                , (4,):  { "Left": set([3]), "Right": set([4]), "Suck": set([4])  }
                , (5,):  { "Left": set([5]), "Right": set([6]), "Suck": set([5])  }
                , (6,):  { "Left": set([5]), "Right": set([6]), "Suck": set([8])  }
                , (7,):  { "Left": set([7]), "Right": set([8]), "Suck": set([7])  }
                , (8,):  { "Left": set([7]), "Right": set([8]), "Suck": set([8])  }
                
                }
        
        return action_results[nodeStateTuple][action]
        
    
    def goal_test(self, nodeStateSet):
        #if all squares are clean, you're done
        if self.get_heuristic_value(nodeStateSet) == 0:
            return True
        return False

    def get_step_cost(self):
        return 1
    
    def get_heuristic_value(self, nodeStateInput):
        #modify to use set
        nodeState = None
        if type(nodeStateInput) is set and len(nodeStateInput) > 1:
            return 999
        elif type(nodeStateInput) is int:
            nodeState = nodeStateInput
        else:
            nodeState = nodeStateInput.pop()
        
        #For this problem, the number of dirts left
        if nodeState < 3:
            return 2
        elif nodeState >= 3 and nodeState < 7:
            return 1
        else:
            return 0
        
        
if __name__ == "__main__":
    print("This is a module for optimization classes.")
    input("\n\nPlease press Enter to exit.")