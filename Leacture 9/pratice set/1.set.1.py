#write a program to defeact worf "twinkle" in the given file "twinkle twinklw little star.txt"

word = "twinkle"
with open("star.txt","r") as f:
    if(word in f.read()):
        print(f"Yes, the word {word} is present")
    else:
        print("the twinkle is not present")