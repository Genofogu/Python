#Write a program to find weather a file is idential & matches the content of anthor file.

with open("donkey.txt","r") as f:
    a = f.read()
with open("donkey copy.txt","r") as f:
    b = f.read()
    if (a == b):
        print("This file alredy exist, Try with another file.")
    else:
        ("Your file is ready fr uploding")
        # if in future i make a fuction then i run it here.
        