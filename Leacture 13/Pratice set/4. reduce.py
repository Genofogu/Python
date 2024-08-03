# Write a program to find the maximum of the number in a lot using the reduce function?

# what i do
from functools import reduce

sums = lambda a,b: a+b
x = [2345,3453,5,35,45,453,45,2131,3,42,3,5,345,3,45,65,56,4,34,5]

print(reduce(sums,x))


# what harry do

def max(n,m):
    if n>m:
        return n
    return m

maxNum = reduce(max,x)
print(maxNum)