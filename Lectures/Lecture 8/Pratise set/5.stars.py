# ***
# **
# *     for n = 3

#---------------------------------------------------------------
#this only work for 3

def star(n):
    for i in range(1,n+1):
        for j in range(2*n-i-2):
            print("*" , end="")
        print("\n", end="")
star(3)

#---------------------------------------------------------------
#this work for every number

def star(n):
    for i in range(n):
        print("*"*(n-i))
star(9)


    
