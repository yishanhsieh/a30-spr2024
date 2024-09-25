# quick
# book,p180: https://legacy.cs.indiana.edu/classes/a310-dgerman/spr2021/readings/polf.pdf

import numpy as np
from termcolor import colored

a = list(np.random.randint(0 , 100, 5)) #randomly pick up 5 integers from 0~100

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[ len(arr) //2]  #pick up the center as the pivot
        left, middle, right = [], [], []
        print(f"pivot: {colored(pivot, "red")}, list: {arr}")
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            elif x > pivot:
                right.append(x)
        print(f"left: {colored(left, 'green')}, middle: {colored(middle, 'red')}, right: {colored(right, 'green')}")
        return quicksort(left) + middle + quicksort(right) #concatente sorted list in every recursion.

print(quicksort(a))
