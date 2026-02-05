# DSC 40B HW9 Problem 4 - Fall 2024
# Author: Issac Roy
from HW9.dsf import DisjointSetForest

def slc(graph, d, k):
    forest = DisjointSetForest(graph.nodes)
    for u, v in sorted(graph.edges, key=d):
        if len(set(forest.find_set(node) for node in graph.nodes)) == k: break
        if forest.in_same_set(u, v): continue
        forest.union(u, v)

    clusters = {}
    for node in graph.nodes:
        root = forest.find_set(node)
        if root not in clusters: clusters[root] = set()
        clusters[root].add(node)
    
    return frozenset(frozenset(cluster) for cluster in clusters.values())