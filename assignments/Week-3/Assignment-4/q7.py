def addition(
    lst1: list[int | float], lst2: list[int | float]
) -> list[int | float] | str:
    total = []

    len_list1 = len(lst1)
    len_list2 = len(lst2)

    if len_list1 != len_list2:
        return "Lists are not of same length"

    for i in range(0, len_list1):
        total.append(lst1[i] + lst2[i])
    return total


lst1 = [10, 25, 30, -10, 1, 9]
lst2 = [58, 11, -15, 20, 6, 1]

result = addition(lst1, lst2)

print(result)
