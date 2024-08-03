#write a program to filter a list of number which is divisible by 5.


# what i do
a = [2345,3453,5,35,45,453,45,2131,3,42,3,5,345,3,45,65,56,4,34,5]

b = lambda x: x/5

c = filter(b,a)
print(list(c))


# what harry done

def div(n):
    if n%5 == 0:
        return True
    return False

f = [2345,3453,5,35,45,453,45,2131,3,42,3,5,345,3,45,65,56,4,34,5]


d = filter(div,f)
print(list(d))