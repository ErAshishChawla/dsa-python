def threeConsecutive(lst: list[int | float]) -> str | list:
    consecutives = []

    for i in range(1, len(lst) - 1):
        if lst[i] == lst[i - 1] and lst[i] == lst[i + 1] and lst[i] not in consecutives:
            consecutives.append(lst[i])

    if len(consecutives) == 0:
        return "No"
    return consecutives


print(threeConsecutive([1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]))
print(threeConsecutive([4, 5, 5, 5, 3, 8]))
print(threeConsecutive([1, 1, 1, 64, 23, 64, 22, 22, 22]))
print(threeConsecutive([54, 1, 4, 56, 67, 879, 22]))
