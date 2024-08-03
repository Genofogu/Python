# find the sum of first n natural number using while loop

i = 0
sum = 0
n = int(input("Write a number:"))
while(i<=n):
    sum += i
    i += 1
print(f"The sum of first {n} natural number is {sum}")
    