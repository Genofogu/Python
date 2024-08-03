class emplooyee:
    a = 10 
    b = 12
    c = 14
    @classmethod
    def setatt(cls,a,b,c):
        cls.a = a
        cls.b = b
        cls.c = c
        
    @property
    def length(self):
        return self.a

emp = emplooyee()
emp.setatt(1,2,3)
print(emp.length)
emp.length = 45
print(emp.length)
