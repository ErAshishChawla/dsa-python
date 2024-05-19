def factorial(n: int) -> int:
    result: int = 1

    i: int = 1
    while i <= n:
        result *= i
        i += 1

    return result


print(factorial(5))
