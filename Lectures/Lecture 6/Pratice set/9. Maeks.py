# Write a program to calculate  the grades of a student from his marls from this fowing scheme:

while True:
    a = int(input("Enter your marks:"))
    if (a<100):
        break
    else:
        print("Marks can't be more than 100")

if(90<a<=100 ):
    print("Ex")
elif(80<a<=90 ):
    print("A")
elif(70<a<=80 ):
    print("B")
elif(60<a<=70 ):
    print("C")
elif(50<a<=60 ):
    print("D")
elif(a<50):
    print("F")

