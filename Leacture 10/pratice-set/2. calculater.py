# when you doen,t have money so dont explore and see the  things on amazon and flipkart to buya nd dont waste the time.

#Write a class calculator capableof  finding square, cube and squareroot of a number.

import math
class Calculator:
    def __init__(self,number) :
        self.number = number
    def square(self):
        return self.number * self.number
    def squareroot(self):
        return math.sqrt(self.number)
    def cube(self):
        return self.number * self.number * self.number
    
number = Calculator(9)
print(number.square())
print(number.squareroot())
print(number.cube())

        