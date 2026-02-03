# DSC 40B HW5 Problem 1 - Fall 2024
# Author: Issac Roy

def max_points_on_line(X, p):
    slopes = {"default": 0}
    for x in X:
        slope = (p[1] - x[1]) / (p[0] - x[0]) if p[0] != x[0] else float('inf')
        slopes[slope] = slopes.get(slope, 0) + 1
    return max(slopes.values())