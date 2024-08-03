# Write a program to cheack wheater a given number is prime or not

a = int(input("Enter a number:"))

for item in range(2,a):
    if (a%item == 0):
        print(f"{a} is not a prime number")
        break
else:
    print(f"{a} is a prime number")
    
    
# loop questions