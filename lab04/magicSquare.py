# magicSquare

# n x n squre
# Sum of elements in each row, column, and two diagonals is the same.
# 
# Write a program that reades 16 values from the keyboard, 
# and tests whehter they are magic square
# 
# 1. Does each of the numbers 1, 2, ...16 occur in the user input?
# 2. Whether the sums of rows, columns, and diagonals are equal?
# 
# Set row = n - 1, column = n / 2.
# 

import random

def magic(n):
    m = []
    for i in range(n):
        m.append([0] * n)
    for k in range(1, n*n, 1):
        i = random.randrange(n)
        j = random.randrange(n)
        m[i][j] = k
    return m

def show(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(("  " + str(m[i][j]))[-3:], end=' ')
        print()

n = int(input("Enter size of matrix: "))
if n%2 == 1:   # it only works for odd numbers
    l = magic(n)
    show(l)
else: 
    print("This is not a valid magic square dimension.")