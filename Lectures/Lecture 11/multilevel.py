# multilevel inheritance

class nte:                        #Parent
    a = 4

class tna(nte):                   #Child
    b = 564
    
class tan(tna):                   #child of child (like: Son of child)
    c = 5
    
dsd = tan()
print(dsd.a)
print(dsd.b)
print(dsd.c)
    