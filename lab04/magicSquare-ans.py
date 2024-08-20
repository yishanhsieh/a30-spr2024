def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Magic square is not possible for even-sized grids.")
    
    magic_square = [[0] * n for _ in range(n)]
    
    # Starting position
    row = n - 1
    column = n // 2
    
    for k in range(1, n * n + 1):
        magic_square[row][column] = k
        
        # Store previous position
        prev_row, prev_column = row, column
        
        # Move to the next position
        row = (row + 1) % n
        column = (column + 1) % n
        
        # If the next position is already filled
        if magic_square[row][column] != 0:
            # Revert to the previous position and move up one row
            row = (prev_row - 1) % n
            column = prev_column

    return magic_square

def print_magic_square(magic_square):
    n = len(magic_square)
    for row in magic_square:
        print(" ".join(f"{num:2}" for num in row))

# Example usage:
n = 3  # You can change n to any odd number
magic_square = generate_magic_square(n)
print_magic_square(magic_square)
