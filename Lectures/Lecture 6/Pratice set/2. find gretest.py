#write the program to find greater of four number enrtered by the user 


a = int(input("enter the number:"))
b = int(input("enter the number:"))
c = int(input("enter the number:"))
d = int(input("enter the number:"))


# my methods

e = [a,b,c,d]
e.sort()
e.reverse()

if("input is given"):
     print(e[0])
else:
     print(None)


# only using if else

if(a>b):
    max1 = a
else:
    max1 = b
    
if(c>d):
    max2 = c
else: 
    max2 = d
    
if(max1>max2):
    final = max1
else:
    final = max2
print(final)