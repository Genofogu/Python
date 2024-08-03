#    *
#   ***       n = 4
#  *****
# *******

# n = int(input("Enter a number:"))
# for i in range(1,n):
#     for j in range(n-i):
#         print(" " , end="")
#     for k in range(2*i-1):
#         print("*" , end="")
#     for l in range(n-i):
#         print(" " , end="")
#     print("\n", end="")
    
# for n = 4

n = 4 
for i in range(1,n+1):
    for j in range(n-i):
        print(" " , end="")
    for k in range(2*i-1):
        print("*" , end="")
    for l in range(n-i):
        print(" " , end="")
    print("\n", end="")
            