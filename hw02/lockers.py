#homework 2 - problem 5

#Can you solve the locker riddle? - Lisa Winer
#https://www.youtube.com/watch?v=c18GjbnZXMw&t=184s

#A school’s lockers are numbered 1 to 100. One hundred students
#enter the school one at a time. The first student opens the lockers.
#The second student closes the even numbered lockers. The third
#student either closes or opens every third locker. The remaining
#students continue the pattern. Write a program to determine
#which lockers remain open at the end, after the last one of the
#students passes. Explain the result. Make sure the program not
#only reports the situation at the end but also conveys the stages
#through which the array of lockers passes.

# reference: https://legacy.cs.indiana.edu/classes/a310-dgerman/spr2024/lab02/lockers.html

# 1st: open locker
# 2nd: close 2,4,6,...
# 3rd: close/open 3,6,9...

lockers = [' '] * 100 #all closed

for student in range(1, 101): #start, stop
    for locker in range(student, 101, student):  #start, stop, step
        if lockers[locker-1] == 'O':  #close the locker if it's open
            lockers[locker-1] = ' '
        else:
           lockers[locker-1] = 'O' # otherwise, open the closed locker
        
print(''.join(lockers))

