a = ['as',2,3,'dfsfs']
i = 0
for item in a:
    print(f"This is the {i} character of {item}")
    i = i+1


# using enumerate 
for i,item in enumerate(a):
    print(f"This is the {i+1} character of {item}")