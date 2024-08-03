class Parent:
    name = "df"
    def __init__(self) :
       print("parent")
    
class child1(Parent):
    name1 = "dfwas"
    def __init__(self) :
       super().__init__()
       print("child1")
    
class child2(child1):
    name2 = "dfdd"
    def __init__(self) :
       super().__init__()
       print("child2")
       
ds = child2()
print(ds.name)
print(ds.name1)
print(ds.name2)
    