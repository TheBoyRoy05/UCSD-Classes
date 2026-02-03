# DSC 40B HW4 Problem 3 - Fall 2024
# Author: Issac Roy

import random

def in_place_partition(arr, start, stop, pivot_ix):
    def swap(ix_1, ix_2):
        arr[ix_1], arr[ix_2] = arr[ix_2], arr[ix_1]
        
    pivot = arr[pivot_ix][0]
    swap(pivot_ix, stop-1)
    middle_barrier = start
    
    for end_barrier in range(start, stop - 1):
        if arr[end_barrier][0] < pivot:
            swap(middle_barrier, end_barrier)
            middle_barrier += 1
            
    swap(middle_barrier, stop-1)
    return middle_barrier
        
def quickselect(arr, k, start, stop):
    pivot_ix = random.randrange(start, stop)
    pivot_ix = in_place_partition(arr, start, stop, pivot_ix)
    
    if pivot_ix == k - 1:
        return arr[pivot_ix]
    elif pivot_ix < k - 1:
        return quickselect(arr, k, pivot_ix + 1, stop)
    else:
        return quickselect(arr, k, start, pivot_ix)

def knn_distance(arr, q, k):
    for i in range(len(arr)):
        arr[i] = (abs(q - arr[i]), arr[i])
        
    return quickselect(arr, k, 0, len(arr))