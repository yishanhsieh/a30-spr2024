#lab01-gold
# Craps is a game played with two dice. 
# Each bet is one chip. 
# The goal is to roll a seven (with two dice)
# The house pays 4 chips plus your orignal chip if you win.

# 6 * 6 --> possible outcomes
# sum 7?
#   - (1,6), (2,5), (3,4) - 6 possibilites
# 6/36 --> 1/6 (win) & 5/6 (lose)

# original = x chips
# expected win =  4/6 * 4 = 2/3 (4/6)
# expected lose = 5/6 * 1 = 5/6
# it's not fair --> you will lose $1/6 (about $0.16)


import random

wins = 0
test = 1000

for times in range(100):
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    sum = d1 + d2
    if sum == 7:
        wins += 4
    else: wins -= 1

print(wins)

