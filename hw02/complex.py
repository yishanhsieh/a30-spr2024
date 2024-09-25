class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        return str(self.real) + "+ i*" + str(self.imag)
    
    def __add__(self,othernum):
        newreal = self.real + othernum.real
        newimag = self.imag + othernum.imag
        return Complex(newreal,newimag)
    
    def __mul__(self,othernum):
        newreal = (self.real*othernum.real)-(self.imag*othernum.imag)
        newimag = (self.real*othernum.imag) + (self.imag*othernum.real)
        return Complex(newreal, newimag)


a = Complex(2,3)
b = Complex(3,5)
print(a * b)

# def main():
#     a = Complex(2,3)
#     b = Complex(3,5)

#     print(a)
#     print("I have two complex numbers: " str(a) + " and " str(b))

#     product = a*b
#     sum = a+b
