def sumAndAvg(lst: list[int]) -> list[int | float]:
    total = 0
    count = len(lst)
    for i in lst:
        total = total + i
    avg = total / count
    return [total, avg]


lst = [34, 11, 91, 59, 33, 22]
print("List:", lst)
print("Sum:", sumAndAvg(lst)[0])
print("Average:", sumAndAvg(lst)[1])
