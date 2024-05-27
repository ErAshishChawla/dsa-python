def commonElements(lst1: list, lst2: list) -> list:
    common_list = []
    for i in lst1:
        if i in lst2:
            common_list.append(i)
    return common_list


lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [78, 14, 23]
x = commonElements(lst1, lst2)
print(x)

lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [11, 78, 14, 23, 34]
x = commonElements(lst1, lst2)
print(x)
