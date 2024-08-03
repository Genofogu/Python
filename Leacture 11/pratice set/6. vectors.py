#write __str__() method yo print the vector as follow:
# 7i+6j+10k
#Assure vector of dimission 3 for this problem.

class vector3d():
    def __init__(self,i,j,k) -> None:
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self) -> str:
        return (f"{self.i}i+{self.j}j+{self.k}k")
    

a1 = vector3d(7,6,10)
print(a1)