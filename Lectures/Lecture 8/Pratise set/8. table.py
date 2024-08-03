# multiplation table

#-------------------------------------------------------------------
  
def table_():
    n = int(input("enter a number:"))
    print(f"Multiplication Table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        
table_()
 

#-------------------------------------------------------------------
#Using list

def multiplication_table_of_10():
    number = 10
    table = []
    for i in range(1, 11):
        table.append(f"{number} x {i} = {number * i}")
    return table

# Example usage
table_of_10 = multiplication_table_of_10()
for line in table_of_10:
    print(line)
