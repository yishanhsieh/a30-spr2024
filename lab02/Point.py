# lab02
# Point.py

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def distanceTo(self, otherPoint):
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y
        return math.sqrt(dx**2 + dy**2)
    
def main():
    a = Point(0, 0)
    b = Point(1, 1)
    #print(a)
    print("I have two point objects:" + str(a) + " " + str(b))
    # I have two point objects: (3, 2) (-1, 5)
    howFar = a.distanceTo(b)
    #print(howFar) # prints 5

    #a = Point(0, 0)
    #b = Point(1, 1)
    print("Distance from " + str(a) + " to " + str(b) + " is: " + str(a.distanceTo(b)))
    # Distance from (0, 0) to (1, 1) is: 1.414213...

if __name__ == "__main__":
    main()