#Make a game that genrates random number  and ask user to guess it.
#if the plyer guess is higer than the actual number the program display 'Choose lower number' similary if the user's guess is too low .the program prints "higher number please"


import random

number = random.randint(1,100)
attempt = 1
player = int(input("Guess the number:"))


while(True):
    if (player>number):
       player = int(input("Choose lower digit:"))
       attempt += 1
    elif (player<number):
       player = int(input("Choose higer digit:"))
       attempt += 1
    else:
        print(f"You take {attempt} attempts to complete this \nYes,The number is {number}.")
        break
        