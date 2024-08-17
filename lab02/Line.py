from Point import Point

class Line(Point):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return "(" + str(self.p1) + ", " + str(self.p2) + ")"
    def length(self):
        distance = self.p2.distanceTo(self.p1)
        return distance
    
def main():
    print("=================Class Line=============")
    a = Point(0,0)
    b = Point(1, 1)
    c = Line(a, b)
    distance = c.length()
    print("Length of Line " + str(c) + " is: ", distance)

if __name__ == "__main__":
    main()
