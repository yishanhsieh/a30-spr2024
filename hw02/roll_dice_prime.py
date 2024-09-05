# Homework 2 - P3
# you roll three dice, what is the chance the sum 
# is not a prime number?

# Total possible results are 6*6*6 = 216
# three dice sum is 3~18
# prime num 3~18 are: 3, 5, 7, 11, 13, 17

# sum = 3, (1,1,1)-1 way
# sum = 5, (1,1,2)-3 ways, (2,2,1)-3 ways => 6 ways
# sum = 7, (1,1,5)-3 ways, (1,2,4)-6 ways, (1,3,3)-3 ways, (2,2,3)-3 ways => 15 ways 
# sum = 11, (1,4,6)-6 ways, (2,3,6)-6 ways, (1,5,5)-3 ways, (3,3,5)-3 ways, (2,4,5)-6 ways, (3,4,4)-3ways => 27 ways
# sum = 13, .... => 21 ways
# sum = 17, ... => 3 ways
# ..... total: 73 ways

# 216 - 73 = 143 (non-prime sum)
# percentage is 143/216 =~ 0.66


# use python to simulate

import numpy as np

prime_numbers = [3, 5, 7, 11, 13, 17]
games = 10000
not_prime_counter = 0

for i in range(games):
    game = np.random.choice([1,2,3,4,5,6], 3)
    sum_game = sum(game)
    if sum_game not in prime_numbers:
        not_prime_counter +=1

print(not_prime_counter / games )


