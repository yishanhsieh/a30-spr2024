import numpy as np
exp = 10000
not_prime_counter = 0


for i in range(exp):
   game_n = np.random.choice(["H", "T"], 100) 
   list_n = ''.join(game_n)
   
   if "H"*6 in list_n or "T"*6 in list_n:
       not_prime_counter +=1

print("Question 4 : Numpy solution -", not_prime_counter / exp)

