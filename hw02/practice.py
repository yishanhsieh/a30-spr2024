import random
numberOfStreaks = 0
for experimentNumber in range(1):
 # Code that creates a list of 100 'heads' or 'tails' values.
    list = []
    for i in range(100):
        game = random.choice(["H", "T"])
        list.append(game)
        list_string = ''.join(list)
    print(list)
    
 # Code that checks if there is a streak of 6 heads or tails in a row.
    if "H"*6 in list_string or "T"*6 in list_string:
       numberOfStreaks += 1
 
print('Question 4: Chance of streak is %s%%' % (numberOfStreaks / 100))
