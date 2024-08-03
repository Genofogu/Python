# Write a program to detect the usrname contaion lessthan 10 words or not 

while True:
    a = input("Enter you user name:")
    if (len(a)<10):
        break
    else:
        print("Username can't be contain more than 10 words")
        print("Try again")

if(len(a)<10):
    print(a)
        


    

