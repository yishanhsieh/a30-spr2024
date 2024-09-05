# scalable four problem
# should be a "4"  # I still can't make it 

#size = int(input("What size: "))
size = 12

for row in range(size):
    for col in range(size):
        if row == size // 2 or col == size //2 or (size//2 - row) == col:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print() #new line

