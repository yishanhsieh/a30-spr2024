# magicSquare

# n x n squre
# Sum of elements in each row, column, and two diagonals is the same.
# 
# Write a program that reades 16 values from the keyboard, 
# and tests whether they are magic square
# 
# 1. Does each of the numbers 1, 2, ...16 occur in the user input?
# 2. Whether the sums of rows, columns, and diagonals are equal?
# 
# Set row = n - 1, column = n / 2.

def magic(size):
    matrix = []
    row = size - 1
    col = size//2
    for i in range(size):
        matrix.append([0] * size)
    for k in range(1, size*size + 1):
        matrix[row][col] = k
        prev_row = row
        prev_col = col
        row+=1
        col+=1
        if row == size:
            row = 0
        if col == size:
            col = 0
        if matrix[row][col] != 0:
            row = prev_row
            col = prev_col
            row -= 1
    return matrix

def show(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(("  " + str(m[i][j]))[-3:], end=' ')
        print()


# n = int(input("Enter size of matrix: "))
# if n%2 == 1:   # it only works for odd numbers
#     l = magic(n)
#     show(l)
# else: 
#     print("This is not a valid magic square dimension.")

show(magic(3))