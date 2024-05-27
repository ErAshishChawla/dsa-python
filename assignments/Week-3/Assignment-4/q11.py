def valuesWithCountGT3(lst: list) -> list:
    result = []

    for i in lst:
        if lst.count(i) > 3 and i not in result:
            result.append(i)

    return result


a = [1, 1, 1, 2, 3, 2, 2, 4, 2, 1, 3, 1, 7, 4, 2]

print("Original List:", a)
print("Values with count greater than 3:", valuesWithCountGT3(a))
