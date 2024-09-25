# lab 04 (https://legacy.cs.indiana.edu/classes/a310-dgerman/fall2022/lab03.html)

# For this lab start by reviewing

# chapters 1-6 in Sweigart (https://automatetheboringstuff.com/)

# De Morgan's Laws
# first law: not(a and b) =  (not a) or (not b)
# second law: not(a or b) =  (not a) and (not b)

'''
 1. Prove that for a and b unknown truth values we have
     not (a and b) == (not a) or (not b)
'''

def lhs(a,b): #left hand side
     return not (a and b)

def rhs(a,b): #right hand side
     return (not a) or (not b)

def q1(a,b):
     return not (a and b) == (not a) or (not b)

'''

 2. Simplify, for a and b unknown truth values
     not ((not a) or (not b))
     
     --> not(not a) and not(not b)

     --> a and b

'''

def q2(a,b):
     return not ((not a) or (not b)) == (a and b)


def main():
     # advanced and quicker way
     la = [0,1]
     lb = [0,1]
     for a in la:
          for b in lb:
               print(a,b, q2(a,b))     
     

     # q1- basic but not smart way
     case1 = q1(0,1)
     case2 = q1(0,0)
     case3 = q1(1,1)
     case4 = q1(1,0)
     
     print(0, 1, case1)
     print(0, 0, case2)
     print(1, 1, case3)
     print(1, 0, case4)


if __name__ == "__main__":
     main()

