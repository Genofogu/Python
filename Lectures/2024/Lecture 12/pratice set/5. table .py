# store the multiplaction table in question number 3 in the table.txt

a = int(input("Enter a number to find table:"))

b = [f"{a}X{i}={a*i}" for i in range(1,10+1) if a]       # hao logic of mine ^_^.
print(b)

with open("mul.txt","w") as f:
    f.write(str(b))
