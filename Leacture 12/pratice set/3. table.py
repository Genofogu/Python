#Write a list comprehension to print a list which contains the multiplaction table of a user entered number.

global a
a = int(input("Enter a number to find table:"))

# for  i in range(1,10+1):
#     print(f"{a}X{i}={a*i}")
#     i+=1

b = [f"{a}X{i}={a*i}" for i in range(1,10+1) if a]       # hao logic of mine ^_^.
print(b)


# what harry done

c = [i*a for i in range(1,10+1)]
print(c)

