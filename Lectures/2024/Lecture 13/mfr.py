from functools import reduce

# Demotration for map
a = lambda x: x*x 
l = [1,4,2,3,9]

print(map(a,l))      #Is not in readable formet like:- str , int , list ,etc

print(list(map(a,l)))


#filter

a = lambda x: x<8
b = [2,12,43,1,2,4,3,4,12,312,3,312,3,23,2,3,13,2,3,23,23,3,213,23,12,32,3,123,2,32,31,3,24,3,5,56,6,5,4,3,3]
c = filter(a,b)
print(list(c))

# reduce

sum = lambda x,y:x+y
i = [32,231,4,3,2]
x = reduce(sum,i)
print(x)