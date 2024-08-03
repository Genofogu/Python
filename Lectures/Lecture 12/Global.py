a = 4
def fun():
    global a    #it update the global value of a
    a = 34
    print(a)
    a = 23
    print(a)
    
print(a)
fun()
print(a)