def fun():
    print("hello")
fun()

#-----------------------------------------------------------------------------------
#Fuction with aruguments

def set(name):
     print(f"Hello {name}")
     
a = set("jerry")
print(a)

#---------------------
# another usage

import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_three(a,b,c):
    return lcm(lcm(a, b),c)

a = int(input("First number:"))
b = int(input("Second number:"))
c = int(input("Third number:"))

print(f"The LCM of {a,b,c} is {lcm_three(a, b, c)}")


#-----------------------------------------------------------------------------------
# i am a build in Module duplicate

# Duplicate of print()
import sys

def a(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    # Join the arguments using the specified separator
    output = sep.join(map(str, args))
    
    # Write the output to the specified file-like object
    file.write(output + end)
    
    # Flush the output if specified
    if flush:
        file.flush()

# Usage
a("Hello", "World!", sep=', ', end='!!!\n')
a(2)

