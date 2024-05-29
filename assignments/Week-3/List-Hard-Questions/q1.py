from typing import List


def isAscending(lst: List[int | float]) -> bool:
    smallest: int | float = lst[0]

    for i in lst:
        if i < smallest:
            return False
    return True


print(isAscending([1, 2, 3, 4, 5]))
print(isAscending([3, 1, 2, 3, 4, 5]))
