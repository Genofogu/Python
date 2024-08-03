class Something:
    clas = 12
    place  = "Cicago"
    nighours = "new yorkers"
    
    @staticmethod                     #this method doesn't required any object.
    def he():                                 
        print(f"The name is")
        
b = Something()
c = b.clas
print(c)
d = b.he()
e = Something.he()                 # this doen't require any object
print(d)
print(e)
    