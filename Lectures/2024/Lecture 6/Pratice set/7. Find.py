a = ["relax", "cadsa", "catapa","bhaubali","katpa ne bhaubali ki jan kyo li", "type 7","ben 10","Gojou","geto","anu","swarnima","yuwai mo"]
name = input("Enter the words:").lower()
names = False

if (a[0] or a[1] or a[2] or a[3] or a[4] or a[5] or a[6] or a[7] or a[8] or a[9] or a[10] or a[11] in name):
    names = True

if (names is True):
    print("Name is avabile")
else:
    print(name)