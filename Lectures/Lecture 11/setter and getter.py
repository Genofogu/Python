class emplooyee:
    a = 10 
    b = 12
    c = 14
    @classmethod
    def setatt(cls,a,b,c):
        cls.a = a
        cls.b = b
        cls.c = c
        
    @property                         #This is a getter
    def length(self):
        return self.a
        
    @length.setter                    # this is a setter
    def length(self,value):
        self.a = value

emp = emplooyee()
emp.setatt(1,2,3)
print(emp.length)
emp.length = 45
print(emp.length)