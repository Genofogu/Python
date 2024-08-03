# add a static methods on problem to greet the user with hello. like "hello your squareroot is"

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
    
    @staticmethod
    def he():                                 
        print(f"hello your answer is ")
    
    
number = Calculator(9)
print(number.he())
sq = number.square()
sqrt = number.squareroot()
cube = number.cube()
print(sq,sqrt,cube)





