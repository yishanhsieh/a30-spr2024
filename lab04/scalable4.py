# scalable four problem
# should be a "4"  # I still can't make it 

size = int(input("What size: "))

for lin in range(size):
    for col in range(size):
        if lin == size -1 or col == 4 or (lin == size // 2 and col < size/2):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()