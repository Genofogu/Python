# Write a recursion function to calculate the sum of first n nutural number

#sum(8) = 1+2+3+4+5+6+7+8
# sum (8) = 8 + sum(7)
# sum(n) = n + sum(n-1)

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
a = sum(2)
print(a)
