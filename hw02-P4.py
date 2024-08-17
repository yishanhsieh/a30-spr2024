#homework02-P4

# throw a coin 100 times what is the chance 
# for six (heads or tails) in a row

import numpy as np

exp = 10000
in_row_counter = 0

for i in range(exp):
    game = np.random.choice(["0", "1"], 100)
    list = ''.join(game)
    if "0"*6 in list or "1"*6 in list:
        in_row_counter +=1

print(in_row_counter/exp)

