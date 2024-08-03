#Write a program to print third, fifth and seventh element from a list using enumerate function.

a = [112,34,"an","asdfs","sw","adsd","always",4,"2gether"]

for index, item in enumerate(a):
    if(index+1 == 3 or index+1 == 5 or index+1 ==7 or index+1 == 9):
        print(item) 