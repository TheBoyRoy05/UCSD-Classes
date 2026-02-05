# DSC 40B HW7 Problem 4 - Fall 2024
# Author: Issac Roy
import dsc40graph

def biggest_descendent(graph: dsc40graph.DirectedGraph, root, value):
    biggest_values = {}
    
    def dfs(node):
        if node in biggest_values: 
            return biggest_values[node]
        
        max_val = value[node]
        for neighbor in graph.neighbors(node): 
            max_val = max(max_val, dfs(neighbor))
        biggest_values[node] = max_val
        return max_val

    dfs(root)
    return biggest_values