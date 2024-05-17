def calSum(start: int, end: int) -> int | str:
    if start > end:
        return "n1 should be smaller"

    i: int = start
    total: int = 0
    while i <= end:
        if i % 5 == 0:
            total += i
        i += 1
    return total


x = calSum(1, 10)
print(x)

y = calSum(43, 68)
print(y)
