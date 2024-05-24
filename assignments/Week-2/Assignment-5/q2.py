def pattern(n: int) -> float:
    total: float = 0
    for i in range(1, n + 1):
        num = 1 / i
        total += num
    return total


print(pattern(5))
