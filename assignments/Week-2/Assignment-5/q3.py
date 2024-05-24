def pattern(x: int, n: int) -> float:
    total: float = 0
    num: int = 1
    for i in range(1, n + 1):
        total = total + x / num
        num = num + 2
    return total


print(pattern(6, 4))
print(pattern(9, 11))
