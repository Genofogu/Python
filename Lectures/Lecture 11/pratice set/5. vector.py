#   Write a class vector represting a vector of n dimissions. overload the + and * operater which calculate the sun and the dot product of them.

# what i do
class Vector:
   def __init__(self,i,j) -> None:
        self.i = i
        self.j = j
        
   def __add__(obj,self):
        print(f"{self.i}i+{self.j}j")
    
   def __mul__(obj,self):
        return Vector(obj.i*self.i*obj.j*self.j)
    
aj = Vector(1,3)


# What he do

class vector:
    def __init__(self,l1) -> None:
        self.dimision = len(l1)
        self.data = l1
        
    def __add__(self,obj):
        mylist = []
        for i in range(len(obj.data)):
            mylist.append(obj.data[i] + self.data[i])
        return vector(mylist)
       
    def __mul__(self,obj):
        dot = 0
        for i in range(len(obj.data)):
            dot += (obj.data[i] * self.data[i])
        return dot
    
    
v1 = vector([1,2,3])
v2 = vector([11,23,31])
v3 = v1+v2
v4 = v1*v2  #v4 is not a vecor its a sclar
print(v4 ) #dot of 2 vector is always scaler
print(v3.data)

