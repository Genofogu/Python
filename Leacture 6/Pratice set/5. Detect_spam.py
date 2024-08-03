# A Spam comment is definded as a text cointaing keyword
# "make a lot of money" "buy now" "Suscribe us" "click this" write a program to deact these.


# a = ["make a lot of money", "buy now", "Suscribe us","click this"]
# b = input("Enter your word:")

# My way

# if ( b == a[0] or b == a[1] or b == a[2] or b == a[3] ):
#     print("This is spam comment")
#     print("Warning...Don't spam")
# else:
#     print(b)

# this way only work on the words not in sentences
    
# another way

a = ["make a lot of money", "buy now", "Suscribe us","click this"]
b = input("Enter your word:").lower()
spam = False

if('buy now' in b):
    spam = True
if('make a lot of money' in b):
    spam = True
if('Suscribe us' in b):
    spam = True
if('click this' in b):
    spam = True
    
if (spam is True):
    print("You wrote something spamy",b,"is a contain spam words")
else:
    print(b)
    

# how can we find which spam word a person use
    