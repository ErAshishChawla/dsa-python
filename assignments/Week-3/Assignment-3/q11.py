from typing import List


def countFactors(n: int) -> int:
    factors = 0

    for i in range(1, n + 1):
        if n % i == 0:
            factors = factors + 1
    return factors


def checkPrime(n: int) -> bool:
    return countFactors(n) == 2


def calculatePrime(lst: List[int]):
    for i in lst:
        if checkPrime(i):
            print(i, end=" ")
    print()


my_list = [34, 11, 91, 59, 33, 22]

calculatePrime(my_list)
