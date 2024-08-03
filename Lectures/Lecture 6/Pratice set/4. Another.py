# Another thinking come in my mind related to question 3 we can type any number more than 100
# now we make it like no-one can enter the value of m1 , m2 , m3 > 100

# so my question is how can we set a fixed value of an input or not mor than that or less than too.

# so the answer we get
# Python's input function doesn't have built-in support for specifying a maximum length like in HTML.

# Another thinking come in my mind related to question 3 we can type any number more than 100
# now we make it like no-one can enter the value of m1 , m2 , m3 > 100

# so my question is how can we set a fixed value of an input or not mor than that or less than too.

# so the answer we get
# Python's input function doesn't have built-in support for specifying a maximum length like in HTML.

while True:
    m1 = int(input("Enter your Physics marks (out of 100): "))
    m2 = int(input("Enter your Math marks (out of 100): "))
    m3 = int(input("Enter your Chemistry marks (out of 100): "))

    # Validate input to ensure marks are within the range [0, 100]
    if m1 <= 100 and m2 <= 100 and m3 <= 100:
        break
    else:
        print("Marks cannot be greater than 100. Please re-enter the marks.")
        print("Please Re-enter the marks")

m = (m1 + m2 + m3) / 3

a = m1 < 33
b = m2 < 33
c = m3 < 33

if m > 40:
    print("You have passed.")
elif a and b and c:
    print("You have failed in Physics, Math, and Chemistry.")
elif a and b:
    print("You have failed in Physics and Math.")
elif b and c:
    print("You have failed in Math and Chemistry.")
elif c and a:
    print("You have failed in Chemistry and Physics.")
elif a:
    print("You have failed in Physics.")
elif b:
    print("You have failed in Math.")
elif c:
    print("You have failed in Chemistry.")
else:
    print("You have failed.")
