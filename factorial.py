def factorial(n):
    if n < 2:
        return 1
    result = n * factorial(n-1)
    return result

n = 5
r = factorial(n)
print(f"Factorial of {n} is {r}")

def yaz():
    print("This is going to be printed")