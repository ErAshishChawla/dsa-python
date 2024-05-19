"""
Create a function that takes two arguments
n1 and n2
return the sum of allnumbers from 1 to n1 that are divisible by n2
"""


def sumOfDiv(n1: int, n2: int) -> int:
    total: int = 0

    i: int = 1

    while i <= n1:
        if i % n2 == 0:
            total += i
        i += 1

    return total


print(sumOfDiv(100, 1))
