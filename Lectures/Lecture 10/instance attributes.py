# a very basic sample class
class Student:
    name = "ram"
    marks = 34
    year = "2nd"
    centre = "delhi"
    place = "n/a"
    def he(sef):                                 #so we need to describe a attribute of function like sef or any othe word
        print(f"The name is {sef.name}")            
   
#a basic obj  
a = Student() 
b = Student()
print(a.marks)
print(a.centre)
a.he()
b.name = "anu"                                    # this is instance attribute which is only valid for an single object
print(b.name)   

a.he()                                             #both are 
Student.he(a)                                      #same thing