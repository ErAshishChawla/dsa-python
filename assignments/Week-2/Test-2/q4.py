def factorial(n: int) -> int:
    fact: int = 1

    for i in range(1, n + 1):
        fact *= i
    return fact


print(factorial(5))
print(factorial(3))
