#Write a class complexnumber to repreted complex numbers, along with overloaded operators + and * which adds and multiples them.


class complexnumber:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
        
    def __add__(obj,self):
        return complex(self.a + obj.a, self.b + obj.b)
    def __mul__(obj,self):
        self.a * self.b
        
        
c1 = complexnumber(5,11)
c2 = complexnumber(4,1)
c3 = c1+c2
print(c3)


