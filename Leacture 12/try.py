try:
    a = int(input("print a number:"))
    b = int(input("print a number:"))
    c = a+b
    
except Exception as e:
    print(f"This problem occurs: {e}")
    
    
# use of else with try   
else:                                                       
    print(f"finally you come to this place | your answer is {c}")
    

 
