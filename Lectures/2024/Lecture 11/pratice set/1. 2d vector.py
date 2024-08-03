# Create a class c-2d vector and use it to create another class represting  3-d vector.

class vecoter2d:
    def __init__(self,i,j) -> None:
        self.i = i
        self.j = j
        
    def PrintVector(self):
        print(f"{self.i}i+{self.j}j")
        
class vecoter3d(vecoter2d):
    def __init__(self,i,j,k) -> None:
        super().__init__(i,j)
        self.k = k
        
    def PrintVector(self):
        print(f"{self.i}i+{self.j}j+{self.k}k")

formula = vecoter2d(1,5)
formula2 = vecoter3d(2,5,6)

formula.PrintVector()
formula2.PrintVector()
