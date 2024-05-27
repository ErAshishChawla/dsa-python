def removeNth(lst: list, index: int):
    if index < 0 or index >= len(lst):
        print("Index does not exist")
        return
    lst.pop(index)


lst = [34, 11, 91, 59, 33, 22]
print(lst)
removeNth(lst, 3)
print(lst)

lst = [34, 11, 91, 59, 33, 22]
removeNth(lst, 67)
print(lst)
