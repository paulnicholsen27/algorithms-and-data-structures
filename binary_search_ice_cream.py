import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):

    first_index = len(arr)
    sorted_arr = sorted(arr)
    while sorted_arr:
        current = sorted_arr.pop()
        match = m - current
        if binary_ice_cream_search(sorted_arr, match):
            current_index = arr.index(current) + 1
            desired_index = arr.index(match) + 1
            if current == match:
                matching_indexes = [i + 1 for i, j in enumerate(arr) if j == current]
                return matching_indexes[:2]
            else:
                return sorted([arr.index(current) + 1, arr.index(match) + 1])
        first_index -= 1
    return False


    



def binary_ice_cream_search(arr, x):
    pivot_index = len(arr) / 2
    if not arr:
        return False
    if arr[pivot_index] == x:
        return True
    elif arr[pivot_index] > x:
        return binary_ice_cream_search(arr[:pivot_index], x)
    else:
        return binary_ice_cream_search(arr[pivot_index + 1:], x)



print(icecreamParlor(2, [1, 1, 5, 3, 2]))

