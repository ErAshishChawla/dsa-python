def countFactors(n: int) -> int:
    count: int = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def checkPrime(n: int) -> bool:
    return countFactors(n) == 2


for i in range(1, 101):
    if checkPrime(i):
        print(i, end=" ")
