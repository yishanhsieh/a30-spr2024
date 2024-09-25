import math
import random

# Point
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
    a = Point(3,2)
    b = Point(-1,5)
    print(a)
    print("I have two point objects: " + str(a) + " " + str(b))
    howFar = a.distanceTo(b)
    print(howFar)

    a = Point(0,0)
    b = Point(1,1)
    print("Distance from " + str(a) + " to " + str(b) + " is: " + str(a.distanceTo(b)))

if __name__ == "__main__":
    main()


# Line
class Line(Point):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return "(" + str(self.p1) + ", " + str(self.p2) + ")"
    def length(self):
        a = self.p2.distanceTo(self.p1)
        return a

def main():
    print("-------------------------Class Line------------------")
    a = Point(3,2)
    b = Point(-1,7)
    c = Line(a,b)
    distance = c.length()
    print("Length of Line ", c, " is: ", distance)

if __name__ == "__main__":
    main()


# Triangle
class Triangle(Point):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def __str__(self):
        return "(" + str(self.p1) + ", " + str(self.p2) + ", " + str(self.p3) + ")"
    def area(self):
        a = self.p2.distanceTo(self.p1)
        b = self.p1.distanceTo(self.p3)
        c = self.p3.distanceTo(self.p2)
        s = (a + b + c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area
    
def main():
    print("-------------------------Class Line------------------")
    a1 = random.randint(-10, 10)
    a2 = random.randint(-10,10)
    b1 = random.randint(-10,10)
    b2 = random.randint(-10,10)
    c1 = random.randint(-10,10)
    c2 = random.randint(-10,10)

    a = Point(a1, a2)
    b = Point(b1, b2)
    c = Point(c1, c2)
    tri = Triangle(a,b,c)
    A = tri.area()
    print("Area of ", tri, " is: ", A)

if __name__ == "__main__":
    main()


# LinkedList
class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data = d
class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    def add(self,d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
    def remove(self,d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    def find(self,d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None    


# BinaryTree
class Node1:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def show(self):
        if self.left == None:
            left = " . "
        else:
            left = self.left.show()
        if self.right == None:
            right = " . "
        else:
            right = self.right.show()
        return "(" + left + " " + str(self.value) + " " + right + ")"