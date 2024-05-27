def findSmallest(lst: list):
    largest = lst[0]

    for i in lst:
        if i < largest:
            largest = i
    return largest


my_list = [34, 11, 91, 59, 33, 22]

x = findSmallest(my_list)
print(x)
