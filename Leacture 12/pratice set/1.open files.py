#Write a program to open three files 1.tst,2.tst,3.tst. if any of these files are not present , a message without exiting the program must be printed promting the same?

try:
    with open("1.tst","r") as f:
        f.read()
    with open("2.tst","r") as x:
        x.read()
    with open("3.tst","r") as y:
        y.read()
        
   
except Exception as e:
    print(f"The error occurs: {e}")

    
print("If you see that you done the problem.")