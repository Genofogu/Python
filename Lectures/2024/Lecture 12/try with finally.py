def f():
    try:
        a = int(input("enter a number:"))
        b = int(input("enter a number:"))
        print(a*b)
        return a*b
    
    except Exception as e:
        print(f"This is a error: {e}")
        return 0                   #after error its return 0
    
    finally:
        print("but this line always be excuted\nThat is the use of finally.")
    
    print("this linje is not excuted because of return 0")
    
f()