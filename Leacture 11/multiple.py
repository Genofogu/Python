# example of multiple inheritance

class Parent1:
    simple = "easa"
    
class Parent2:
    pimple  = "isa"
    
class Maula(Parent1,Parent2):
    afor = "dasa"

re = Maula()
print(re.simple)
print(re.pimple)
print(re.afor)

    
