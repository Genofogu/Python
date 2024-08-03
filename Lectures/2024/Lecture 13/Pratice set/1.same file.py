# Write a program to input name, marks and phone number of a student and formet it using the formet function like bellow: "the name of the student is harry his marks is 72 and phone number is 9999988888"

a = input("Enter the student name:")
b = input("Enter the student marks:")
c = input("Enter the student phone number:")

d = "the name of the student is {} his marks is {} and phone number is {}".format(a,b,c)
print(d)