#homework02-P4 -p107

# throw a coin 100 times what is the chance 
# for six (heads or tails) in a row

import numpy as np

exp = 100000
in_row_counter = 0

for i in range(exp):
    game = np.random.choice(["0", "1"], 100)
    list = ''.join(game)
    
    if "0"*6 in list or "1"*6 in list:
        in_row_counter +=1

print(in_row_counter/exp)




import random
numberOfStreaks = 0

for experimentNumber in range(10000):
 # Code that creates a list of 100 'heads' or 'tails' values.
    list1 = []
    for i in range(100):
        game = random.choice(["0", "1"])
        list1.append(game)
        list_string= ''.join(list1)
    
 # Code that checks if there is a streak of 6 heads or tails in a row.
    if "0"*6 in list_string or "1"*6 in list_string:
        numberOfStreaks +=1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))