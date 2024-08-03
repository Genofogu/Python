def factorial(n):
    #base condition
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = 23
a = factorial(n)
print(a)



#in the factorail form

def factorial_recursive_with_steps(n):
    if n == 0:
        return "1", 1
    else:
        steps, result = factorial_recursive_with_steps(n - 1)
        return f"{n}x{steps}", n * result

# Get the steps and the result for factorial of 12
steps, result = factorial_recursive_with_steps(12)

# Example usage
print(f"The factorial of 12 is {steps} = {result}")

