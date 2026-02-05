# DSC 40B HW6 Problem 3 - Fall 2024
# Author: Issac Roy

import dsc40graph

def assign_good_and_evil(graph: dsc40graph.UndirectedGraph):
    labels = {}
    def bfs(node):
        queue = [node]
        labels[node] = 'good'
        while queue:
            current_node = queue.pop(0)
            opposite = 'evil' if labels[current_node] == 'good' else 'good'
            
            for neighbor in graph.neighbors(current_node):
                if neighbor not in labels:
                    queue.append(neighbor)
                    labels[neighbor] = opposite
                elif labels[neighbor] == labels[current_node]:
                    return False
        return True
                    
    for node in graph.nodes:
        if node not in labels:
            if not bfs(node): 
                return None
            
    return labels