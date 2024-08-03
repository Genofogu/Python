# Write a function to convert the tempture celsuis to fahrenheit.

def temp(c):
    return (c*9/5)+32

c = int(input("Enter a number:"))
a = temp(c)
print(f"{c}°C = {a}°F")