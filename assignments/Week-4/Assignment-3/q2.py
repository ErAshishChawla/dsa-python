def repeatedItems(tup: tuple) -> list:
    repeated_Items = []

    for i in tup:
        if tup.count(i) > 1 and i not in repeated_Items:
            repeated_Items.append(i)

    return repeated_Items


print(repeatedItems((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9)))
