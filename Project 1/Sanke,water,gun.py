import random

def spw(player,computer):
    if computer == player:
        return None
    if(computer=='s' and player=='p'):
        return True
    elif(computer=='p' and player=='w'):
        return True
    elif(computer=='w' and player=='s'):
        return True
    else:
        return False

a = ["s","p","w"]
computer = random.randint(0,2)
computer = a[computer]
player = input("Write Either 's' or 'p' or 'w':")

if player("s" or "p" or "w"):
    print(f"You chose:{player}")
else:
    print("Invalid Character")


win = spw(player,computer)
if win is None:
    print("Draw")
elif win:
    print("You won")
else:
    print(f"You chose {player} and computer chose {computer}")
    print("You lose")