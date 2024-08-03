class number:
   def __init__(self,a,name):
      self.a = a
      self.name = name
      
   def __add__(self,obj):
       return self.a + obj.a
   
   def __str__(self) -> str:
       return self.name
   
   def __len__(self):
       return self.a
   
a = number(34, "an")
b = number(30, "sw")

print(a+b)
print(a,b)
print(len(a))
print(len(b))