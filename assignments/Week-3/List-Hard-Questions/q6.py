def difference(list1: list, list2: list) -> list:
    difference_list = []

    for i in list1:
        if i not in list2 and i not in difference_list:
            difference_list.append(i)
    return difference_list


print(difference([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print(difference([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
print(difference([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
print(difference([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
