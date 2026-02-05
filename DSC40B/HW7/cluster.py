# DSC 40B HW7 Problem 5 - Fall 2024
# Author: Issac Roy
import dsc40graph

def cluster(graph: dsc40graph.UndirectedGraph, weights, level):
    def bfs(graph, source, status):
        status[source] = 'pending'
        pending = [source]
        visited = []
        
        while pending:
            u = pending.pop(0)
            for v in graph.neighbors(u):
                if status[v] == 'undiscovered' and weights(u, v) >= level:
                    status[v] = 'pending'
                    pending.append(v)
            status[u] = 'visited'
            visited.append(u)
        return visited
    
    status = {node: 'undiscovered' for node in graph.nodes}
    clusters = []
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            clusters.append(frozenset(bfs(graph, node, status)))
            
    return frozenset(clusters)