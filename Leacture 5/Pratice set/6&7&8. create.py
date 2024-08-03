#6. Create an empty  dict allow 4 friends to enter their  favroite language  as a value and use key as their name. assume that the name are unique.

disct = {}
for i in range(4):
    a = input("Enter you name:")
    b = input("Enter yu fav language:")
    disct.update({a:b})
print(disct)


#7. Now if two and other friend name is same so what happend in this program.

# if we have mulitple same keys only on print

#8. Now if two and other friend language is same so what happend in this program.

# all values print

