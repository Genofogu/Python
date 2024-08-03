#Write a function to dectect the greater of the 3 numbers

def threenumbers(a,b,c):
    if (a>b):
        greater = a
    else:
        greater = b
    if (greater<c):
        greater = c

    return(greater)

a = threenumbers(5,3,8)
print(a)