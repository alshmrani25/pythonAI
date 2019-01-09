# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:01:44 2018

@author: domje
"""

from queue import PriorityQueue

#NOTE - if you set the "get_astar_heurustic_cost" function to always return zero,
#then this is a standard Uniform Cost Search
def astar_search(problem):
    frontier = PriorityQueue()
    explored = set()
    node = problem.initial_node
    inital_node_path_cost = problem.get_astar_heuristic_cost(node)
    frontier.put((inital_node_path_cost, node))    
    while True:
        if frontier.empty():
            return None
        node = frontier.get()[1]
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        new_states = problem.expand_node(node.state)
        for state in new_states:
            childNode = node.get_child_node(problem, state)
            childNode_path_cost = childNode.path_cost + problem.get_astar_heuristic_cost(childNode)
            if childNode.state not in explored and childNode.state not in list(frontier.queue):
                frontier.put((childNode_path_cost, childNode))
            elif childNode.state in list(frontier.queue):
                existing_child = frontier[childNode]
                existing_child_path_cost = existing_child.path_cost + problem.get_astar_heuristic_cost(existing_child)
                if existing_child_path_cost > childNode_path_cost:
                    del frontier[existing_child]
                    frontier.put((childNode_path_cost, childNode ))

def get_solution_path(finalNode):
    node = finalNode
    path = []
    while True:
        path.append((node.state, node.path_cost))
        if node.parent:
            node = node.parent
        else:
            path.reverse()
            return path

if __name__ == "__main__":
    print("This is a module for searching methods.")
    input("\n\nPlease press Enter to exit.")