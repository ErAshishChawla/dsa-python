def sumOfSquares(n: int) -> int:
    total: int = 0

    for i in range(1, n + 1):
        total = total + i**2
    return total


print(sumOfSquares(5))
