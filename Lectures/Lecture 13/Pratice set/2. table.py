#the list contaion multiplaction table of 7. Write a program to convert it to a vertical string of same number.

a = [i*7 for i in range(1,10+1)]
st = ""
for item in a:
    st += str(item) + '\n'
    
print(st)