#write a program to accpect marks of 6 students and display them in a shorted manner

import time

a = int(input("Write a first Marks:"))
b = int(input("Write a second Marks:"))
c = int(input("Write a thrid Marks:"))
d = int(input("Write a fourth Marks:"))
e = int(input("Write a fifth Marks:"))
f = int(input("Write a sixth Marks:"))
g = int(input("Write a seventh Marks:"))

marks = [a,b,c,d,e,f,g]
print("Genarating...")
time.sleep(1)
print("Shorting the marks...")
time.sleep(2)
marks.sort()
print(marks)