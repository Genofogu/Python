# override the __len__() methon on vector of problem 5 to display the dimension of the vector

class vector:
    def __init__(self,l1) -> None:
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
    
    def __len__(self):
        return len(self.data)
    
    
v1 = vector([1,2,3])
v2 = vector([11,23,31])
v3 = v1+v2
v4 = v1*v2  #v4 is not a vecor its a sclar
print(v4 ) #dot of 2 vector is always scaler
print(v3.data)

print(len(v3))
