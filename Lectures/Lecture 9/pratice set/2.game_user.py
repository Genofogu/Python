# the game() function in a program lets a user play a game and return a scroce as an integer. you need to reead a file "score.txt" hich is either blank or contaions the previous hi-score . you need to write a program to update the hi-score whenever game() break the high score.


# my-------------------------------
# player = int(input("Enter your high score:"))
# a = int(open("score.txt","r"))
# with open ("score.txt","r") as f:
#     if(player>a):
#        f.write(player)
#        f.close
#     else:
#         print(f"Your score:{player}. High score:{a}")


# --------------------------------------------------------
import random

#game
def game():
    score = random.randint(1,100)
    print(f"this is score:{score}")
    return score


# detection
score = game()
with open("hiscore.txt","r") as f:
    hiscore = f.read()
    h = int(hiscore)
    
if score>h:
    with open("hiscore.txt","w") as f:
        f.write(str(score))
    
 