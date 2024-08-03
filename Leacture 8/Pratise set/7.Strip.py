# Write a python function to remove a given word from the list and step it at the same time.

def word(l,word):
    word = word.strip()
    l.remove(word)
    return l

lists = ["asas","dsfsf","dfsfs",'d']

a = word(lists,"asas")
print(a)    
    