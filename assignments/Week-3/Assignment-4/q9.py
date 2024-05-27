def addSeconds(lst: list[int | float]) -> float:
    return lst[1] + lst[-2]


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(addSeconds(lst))
