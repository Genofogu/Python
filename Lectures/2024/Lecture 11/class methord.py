class emplooyee:
    a = 10 
    b = 12
    c = 14
    @classmethod
    def setatt(cls,a,b,c):
        cls.a = a
        cls.b = b
        cls.c = c
        
        

emp = emplooyee()
emp.setatt(1,2,3)
