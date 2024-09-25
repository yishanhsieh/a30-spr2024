# Solve the letter grade conversion problem

# translate a letter grade into a number grade.
# Letter grade: A, B, C, D, F, with + or -

# A+ = 4, A = 4, A- = 3.5
# B+ = 3.3, B =3, B- = 2.7
# C+ = 2.3, C = 2, C- = 1.7
# D+ = 1.3, D = 1, D- = 0.7
# F = 0

# translate a number into the closet letter grade
# break ties for the better grade
# 2.8 -> B-
# 2.85 -> B

def letter(grade):
    if grade >4 or grade < 0:
        return "Entry cannot be over 4 or below 0."
    elif grade == 4:
        return "A+"
    elif grade >= 3.85:
        return "A"
    elif grade >= 3.5:
        return "A-"
    elif grade >= 3.15:
        return "B+"
    elif grade >= 2.85:
        return "B"
    elif grade >= 2.5:
        return "B-"
    elif grade >= 2.15:
        return "C+"
    elif grade >= 1.85:
        return "C"
    elif grade >= 1.5:
        return "C-"
    elif grade >= 1.15:
        return "D+"
    elif grade >= 0.85:
        return "D"
    elif grade >= 0.5:
        return "D-"
    else: return "F"


print(letter(4.1))
print(letter(3.89))
print(letter(3.7))
print(letter(3.61))
print(letter(3.4999))
print(letter(3.5001))
print(letter(1.65))
print(letter(0.7))
print(letter(0.6999))


