def factorial(n: int) -> int:
    fact: int = 1

    for i in range(1, n + 1):
        fact *= i
    return fact


def sumPattern(n: int) -> float:
    total: float = 0

    for i in range(1, n + 1):
        total = total + 1 / factorial(i)

    return total


print(sumPattern(5))
