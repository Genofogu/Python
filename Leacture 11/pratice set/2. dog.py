# create a class pets from a class animals and futhers create class dog from Pets. Add a method bark to class Dog?

class Animal:
    def __init__(self) -> None:
        pass

class Pets(Animal):
    def __init__(self) -> None:
        super().__init__()
        pass
    
class Dog(Pets):
    def __init__(self) -> None:
        super().__init__()
    def bark(self):
        print("Bhauuu Bhauuu")
            
      
a = Dog()
a.bark