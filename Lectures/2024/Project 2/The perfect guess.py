#my mind making that much big still not workin well. i need to lern more about loops i forget many time to usign ture and which is big and which not so bogling thing  is that ^_^.

import random

number = random.randint(1,100)
player = int(input("Guess the number:"))


while(player):
    if (player>number):
       lowerdigit = int(input("Choose lower digit:"))
    elif (player<number):
       higherdigit = int(input("Choose higer digit:"))
    else:
        print(f"HURH!!! Your guess is corect you and computer both choose{number}")
        
    if (lowerdigit<number):
       l2 = int(input("Choose lower digit again:"))
    elif (number>lowerdigit):
       l2 = int(input("Choose higer digit again:"))
    elif (higherdigit<number):
       h2 = int(input("Choose higer digit again:"))
    elif (number>higherdigit):
       h2 = int(input("Choose lower digit again:"))
    else:
        print(f"HURH!!! Your guess is corect you and computer both choose{number}")
        
    if (l2<number):
       l3 = int(input("Choose lower digit again:"))
    elif (number>l2):
       l3 = int(input("Choose higer digit again:"))
    elif (h2<number):
       h3 = int(input("Choose higer digit again:"))
    elif (number>h2):
       h3 = int(input("Choose lower digit again:"))
    else:
        print(f"HURH!!! Your guess is corect you and computer both choose{number}")
        
    if (l3):
        print(f"You lose the number is {number}")
    elif (h3):
       print(f"You lose the number is {number}")
    else:
        print(f"You lose the number is {number}")
 
        