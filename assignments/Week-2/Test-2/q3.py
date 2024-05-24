def sumNum(n1: int, n2: int):
    total: int = 0

    for i in range(n1, n2 + 1):
        if i % 2 == 0 and i % 7 == 0:
            total += i

    if total == 0:
        return -1
    return total


print(sumNum(1, 30))
print(sumNum(1, 10))
