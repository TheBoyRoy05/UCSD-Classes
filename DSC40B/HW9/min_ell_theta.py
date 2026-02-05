# DSC 40B HW9 Problem 5 - Fall 2024
# Author: Issac Roy

def learn_theta(data, colors):
    max_blue = float('-inf')
    for d, c in zip(data, colors):
        if c == 'blue': max_blue = max(max_blue, d)
    return max_blue

def compute_ell(data, colors, theta):
    total = 0
    for d, c in zip(data, colors):
        total += d <= theta if c == 'red' else d > theta
    return total

def minimize_ell(data, colors):
    losses = {theta: compute_ell(data, colors, theta) for theta in data}
    return min(losses, key=losses.get)

def minimize_ell_sorted(data, colors):
    counter = 0
    min_count = float('inf')
    blue_gt_theta = len(data) / 2
    for d, c in zip(data, colors):
        blue_gt_theta -= (c == 'blue')
        counter += 1 if c == 'red' else -1
        if counter < min_count:
            min_count = counter
            theta = d
    return theta