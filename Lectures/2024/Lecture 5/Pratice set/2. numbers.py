#Write a program to input 8 numbers from the user a display all the unquies(onces.)

# Simple Way
# a = int(input("Enter your Number:"))
# b = int(input("Enter your Number:"))
# c = int(input("Enter your Number:"))
# d = int(input("Enter your Number:"))
# f = int(input("Enter your Number:"))
# g = int(input("Enter your Number:"))
# h = int(input("Enter your Number:"))

# myset = {a,b,c,d,f,g,h}
# print(myset)


#Using for loop

s = set()
for i in range(8):
    s.add(input("Enter your Number:"))
print(s)
