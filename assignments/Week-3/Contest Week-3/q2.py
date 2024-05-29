def countFactors(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def isPrime(n: int) -> bool:
    return countFactors(n) == 2


def notPrimeNumbers(n1: int, n2: int) -> None:
    for i in range(n1, n2 + 1):
        if not isPrime(i):
            print(i, end=" ")
    print()


notPrimeNumbers(5, 20)
