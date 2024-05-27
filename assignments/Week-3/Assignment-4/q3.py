def hasCommonElement(lst1: list, lst2: list) -> bool:
    for i in lst1:
        if i in lst2:
            return True
    return False


lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [78, 14, 23]
x = hasCommonElement(lst1, lst2)
print(x)

lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [78, 14, 23, 34]
x = hasCommonElement(lst1, lst2)
print(x)
