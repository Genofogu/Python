#Can you cahnge the self parameter inside a class to somthing else (say"hello"). try changing self to 'slf' and see the effects.



class parameter:
    def __init__(self):
        self.a = 78
        
ram = parameter()
print(ram.a)



class parameter:
    def __init__(slf):
        slf.a = 78
        
ram = parameter()
print(ram.a)


# seems no change after doing this , yes nothing  change but just it make code not that much readable aother wise no problem