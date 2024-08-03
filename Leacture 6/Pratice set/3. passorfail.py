# Write a program to find if a stdent is pass and fail. if it require 40% ant at least 33% on each subject to pass. Assume  subject and take marks as an input from the user

# m1 = int(input("Enter you Physics marks:"))
# m2 = int(input("Enter you math marks:"))
# m3 = int(input("Enter you Chemistry marks:"))

# m = (m1+m2+m3)/3

# if (m>40):
#     if(m1>33 and m2>33 and m3>33):
#         print("your are pass")
#     else:
#         print("you are fail in one subjext")
# else:
#     print("you are fail")
    
    
    
# on another way with some conditions came in my mind

# m1 = int(input("Enter you Physics marks:"))
# m2 = int(input("Enter you math marks:"))
# m3 = int(input("Enter you Chemistry marks:"))

# m = (m1+m2+m3)/3 

# if(m>40):
#     print("You are pass")
# elif(m1<33):
#     print("you are fail in Physics")
# elif(m2<33):
#     print("you are fail in Math")
# elif(m3<33):
#     print("you are fail in Chemistry")
# else:
#     print("You are fail")


# another methord with all possible conditions :)

m1 = int(input("Enter you Physics marks:"))
m2 = int(input("Enter you Math marks:"))
m3 = int(input("Enter you Chemistry marks:"))

m = (m1+m2+m3)/3 

a = m1<33
b = m2<33
c = m3<33

if(m>40):
    print("You are pass")
elif(a and b and c):
    print("you are fail")
elif(a and b):
    print("you are fail in Physics and math")
elif(b and c):
    print("you are fail in Math and Chemistry")
elif(c and a):
    print("you are fail in Chemistry and Physics")
elif(a):
    print("you are fail in Physics")
elif(b):
    print("you are fail in Math")
elif(c):
    print("you are fail in Chemistry")
else:
    print("You are fail")
    


