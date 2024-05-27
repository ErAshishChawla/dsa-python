def removeDuplicates(lst: list[int]) -> list[int]:
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


a = [1, 1, 1, 2, 3, 2, 2, 4, 2, 1, 3, 1]

print("Original List:", a)
print("List after removing duplicates:", removeDuplicates(a))
