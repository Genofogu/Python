#Write a program to display a/b where a and b are integers. if b=0,display inifine handling the zeroDivission.

# what i do:

try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    if b == 0:
        raise Exception("infinte")
    
    c = (a/b)
    print(c)

except Exception as e:
    print({e})
    
    
# what harry do:

try:
    a = int(input("print a number:"))
    b = int(input("print a number:"))
    c = a/b
    
except ValueError:
    print("This is a value error")
except ZeroDivisionError:
    c = "Infinate"
except Exception as e:
    print(f"This problem occurs: {e}")
    
print(c)
    
    
