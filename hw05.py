# homework 5
# https://legacy.cs.indiana.edu/classes/a310-dgerman/fall2022/hw03.html

# 1. What does round(...) return when applied to ±2.1, ±2.9? (Four cases)

def round_fuc(num):
    a =  round(num)
    print(a)

#round_fuc(2.1)
#round_fuc(-2.1)
#round_fuc(2.9)
#round_fuc(-2.9)

# 2. Same question but this time as it applies to int(...). Use assert to test.

def int_fuc(num):
    a = int(num)
    print(a)
    #Test whehter a condition returns True, 
    # if not, it will return AssertionError.
    assert type(a) == float, 'Not Float'  

int_fuc(2.1)
int_fuc(-2.1)

# 3.Evaluate: list(range(12, 16)), 
# list(range(0, 10, 2)), and list(range(5, -1, -1)).


