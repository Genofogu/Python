l1 = [4,9,3]
l2 = []
for item in l1:
    l2.append(item*item) 
print(l2)  

l2 = [i*i for i in l1 if i>2]
print(l2)