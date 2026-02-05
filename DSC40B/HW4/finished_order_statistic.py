# DSC 40B HW4 Problem 2 - Fall 2024
# Author: Issac Roy

def order_statistic(node, k):
    if node.left is None:
        left_size = 0
    else:
        left_size = node.left.size

    order = left_size + 1

    if order == k:
        return node.key
    elif order < k:
        return order_statistic(node.right, k - order)
    else:
        return order_statistic(node.left, k)
