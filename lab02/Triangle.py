from Point import Point
from Line import Line
import math

class Triangle:
    def __init__(self, p1, p2, p3):
        self.l1 = Line(p1, p2)
        self.l2 = Line(p2, p3)
        self.l3 = Line(p3, p1)
    def __str__(self):
        return "triangle (" + str(self.l1.p1) + ", " + str(self.l2.p1)  + ", " + str(self.l3.p1) + ")"
    def area(self):
        # From Heron's Formula
        # s(aka. half of triangle perimeter) = (a+b+c)/2
        # area = √s(s-a)(s-b)(s-c)
        a = self.l1.length()
        b = self.l2.length()
        c = self.l3.length()
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area


def main():
    print("==============Class Triangle=============")
    a = Point(4,5)
    b = Point(2,2)
    c = Point(5,1)
    tri = Triangle(a,b,c)
    Area = tri.area()
    print("Area of", tri, "is: ", Area)

if __name__ == "__main__":
    main()
    