import random


#is the game of craps fair?

def craps(x):
    player_chips = 100                                      #<-------- player buys in for 100 chips
    count = 0                                               #<-------- variable representing how many hands have been played
    wins = 0
    while count < x:                                        #<-------- keeps running until we have ran however many hands as we want ("")
        player_chips = player_chips - 1                     #<-------- each hand costs 1 chip to play
        dice = random.randint(1,6) + random.randint(1,6)    #<-------- random 2 dice rolls
        if dice == 7:
            player_chips = player_chips + 4                 #<-------- payout if won
            wins = wins + 1
        count = count + 1                                   #<-------- hand complete, add to hand count   
    if player_chips < 100:
        print("Not fair! Player left with " + str(player_chips) + " chips left after " + str(x) + " hand(s)." + str(wins))
    else:
        print("Fair! Player left with " + str(player_chips) + " chips left after " + str(x) + " hand(s).")
print(craps(300))


#what are the odds of rolling a prime number when rolling 3 dice?

def prime_dice_roll(x):          #<--------- 'x' is the amount of tests you want to try
    prime = 0
    non_prime = 0
    count = 0
    prime_numbers = [3,5,7,11,13,17]
    non_prime_numbers = [4,6,8,9,10,12,14,15,16,18]
    while count < x:
        dice_total = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        if dice_total in prime_numbers:
            prime = prime + 1
        elif dice_total in non_prime_numbers:
            non_prime = non_prime + 1
        count = count + 1
    print("Prime roll count is " + str(prime) + " and Non-Prime roll count is " + str(non_prime) + " after " + str(x) + " roll(s).")
print(prime_dice_roll(100000))


# which lockers are still open?

lockers = ['c'] * 100
for student in range(1,101):
    for locker in range(student, 101, student):
        if lockers[locker-1] == 'c':
            lockers[locker-1] = 'open'
        else:
            lockers[locker-1] = 'c'
print(lockers)


#streaks of Heads or Tails?

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    count = 0
    list_of_H_or_T = []
    while count < 100:
        list_of_H_or_T.append(random.randint(0,1))
        count = count + 1

    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak_H = 0
    streak_T = 0
    internal_streak_counter = 0
    for i in list_of_H_or_T:
        if i == 0:
            streak_H = streak_H + 1
            streak_T = 0
        else:
            streak_T = streak_T + 1
            streak_H = 0
        if streak_H == 6:
            streak_H = 0
            internal_streak_counter = internal_streak_counter + 1
        if streak_T == 6:
            streak_T = 0
            internal_streak_counter = internal_streak_counter + 1
    if internal_streak_counter > 0:
        numberOfStreaks = numberOfStreaks + 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))




# Complex Number Problem

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    


# Creature Class Problem

class Creature:
    def __init__(self, name):
        self.name = name
        print("Creature " + self.name + " created.")
    def talk(self):
        return "My name is " + self.name + " and I am a " + type(self).__name__ + self.makeSound();
    def makeSound(self):
        return ""
    
# from Creature import Creature      <----------- Would use this if the creature code was in a different file

class Dog(Creature):
    def __init__(self, name):
        super().__init__(name)
    def makeSound(self):
        return ": woof."
    
class Cow(Creature):
    def __init__(self, name):
        super().__init__(name)
    def makeSound(self):
        return ": moo."
    
#      in the window when you run the file, you can create a creatur by saying x = Creature("*name*"),
#      which returns: Creature *name* created. When typing in x.talk, the code will return: My name is *name* and I am a Creature.
#      when saying x = Dog("Buster"), it returns Creature Buster Created, When saying x.talk, it returns My name is Buster and i am a Dog: woof.