import random


def problem4():
    # Coin Flip Streaks
    numberOfStreaks = 0
    for experimentNumber in range(10000):
        coin_flip = []
        for i in range(100):
            coin_flip.append(random.randint(0,1))

        streak = 1
        for i in range(1, len(coin_flip)):
            if coin_flip[i] == coin_flip[i-1]:
                streak += 1
            else:
                streak = 1
            if streak == 6:
                numberOfStreaks += 1
                break
    return str(numberOfStreaks/100) + '%'

print(problem4())