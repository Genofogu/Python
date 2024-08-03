#Write a program to all the persons names stored in a list  L1

l1 = ["harry","sohan","sachin","rahul"]
a = 0
b = len(l1)

while(a<b):
    print("Good moring",l1[a])
    a += 1
    
    
print("Only for which starts with s....")

for items in l1:
    if items.startswith("s"):
        print("Special Good morning for",items)
        print(f"Special Good morning for {items}")
        