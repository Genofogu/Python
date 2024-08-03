#Write a program to find out the line number where python is present from question 6.

a = "python"
i = 0
with open("log.log","r") as l:
       f = l.read()

while(f):
    with open("log.log","r") as l:
        g = l.readlines()
        print(g)
        break
while(i<len(g)):
    x = g[i]
    print(x)
    i += 1
        
           
           