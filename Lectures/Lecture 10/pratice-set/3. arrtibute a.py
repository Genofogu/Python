#Create a class with attribute a ; create an object from it and set a directily using object from it and set a directly using a = 0. does this  cahnge the class attribute.

# answer is no   explation giveing bellow:
class han:
    a = 9

harry = han()
print(harry.a)
harry.a = 0                #I am setting instence attribute using this not class attribute.
print(harry.a)



#Here how we set class attribute.
print(han.a)
han.a = 0                  
print(han.a)