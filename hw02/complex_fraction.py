#homework02


#Develop a Complex number class with + and *. Please refer to the development
#of class Fraction from our text, by Miller and Ranum

#reference:  https://runestone.academy/ns/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-fractioncode


class Complex:  # (a + bi)
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + " * i"
    def __add__(self, other):        
        return Complex(self.real + other.real, self.imag + other.imag)
    
class Fraction:
    def __init__(self, num, den):
        self.num = num #numerator
        self.den = den #denominator
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def __add__(self, other):
        return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)
    


f1 = Fraction(3,4)
f2 = Fraction(-2, 5)
print(f1 + f2)

c1 = Complex(3,5)
c2 = Complex(-3, -5)
print(c1 + c2)

# The following is the code from Miller's book about Fraction class

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

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
