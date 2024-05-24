def countFactors(n: int) -> int:
    count: int = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def checkPrime(n: int) -> bool:
    return countFactors(n) == 2


def printPrimeFactors(n):
    for i in range(1, n + 1):
        if n % i == 0 and checkPrime(i):
            print(i, end=" ")
    print()


printPrimeFactors(20)
printPrimeFactors(7)
printPrimeFactors(72)
