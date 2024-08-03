try:
    a = int(input("print a number:"))
    if a>500:
        raise Exception("a is too large")
    
    
    b = int(input("print a number:"))
    if b>500:
        raise Exception("b is too large")
    
    c = a+b
    print(c)
    
except Exception as e:
    print(f"This problem occurs: {e}")