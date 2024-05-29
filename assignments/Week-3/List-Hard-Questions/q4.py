def checkPalindrome(lst: list) -> bool:
    reversed_list = []

    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])

    for i in range(0, len(lst)):
        if lst[i] != reversed_list[i]:
            return False
    return True


print(checkPalindrome([1, 2, 3, 2, 1]))
print(checkPalindrome([1, 2, 3, 4, 5]))
