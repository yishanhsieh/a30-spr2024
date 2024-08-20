# leap year

# a leap year = 366 days/year
# year > 1582, follow Julian Calendar Leap Year Rules --> % 4 == 0
# year / 4, year / 400
# NOT year / 100
# use if and Boolean

class Year:
    def __init__(self, year):
        self.year =  year

    def isLeapYear(self):
         if self.year < 1582 and self.year % 4 ==0:
             return str(self.year)+ " is a LY."
         elif (self.year % 400 == 0 or self.year % 4 == 0) and (self.year % 100 != 0):
              return "{} is a Leap Year.".format(self.year)
         else: return "{} is NOT a Leap Year.".format(self.year)
         
is_LY = Year(1500)
result = is_LY.isLeapYear()
print(result)

# ===== German's solution
class Leap:
     def isLeapYear(year):
          if year < 1582:
               return year % 4 == 0
          else:
             if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
             else:
                return False
             
a = Leap.isLeapYear(2000)
b = Leap.isLeapYear(1500)
c = Leap.isLeapYear(2500)
print(a,b, c)