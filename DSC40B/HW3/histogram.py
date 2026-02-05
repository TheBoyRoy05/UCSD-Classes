# DSC 40B HW3 Problem 3 - Fall 2024
# Author: Issac Roy

def histogram(points, bins):
    res = []
    curr_bin = 0
    num_points = 0
    calc_density = lambda: num_points / (len(points) * (bins[curr_bin][1] - bins[curr_bin][0]))
    
    for point in points:
        if point >= bins[curr_bin][1]: 
            res.append(calc_density())
            curr_bin += 1
            num_points = 0
        num_points += 1
    res.append(calc_density())
    return res