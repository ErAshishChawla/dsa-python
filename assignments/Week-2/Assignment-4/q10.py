def factorCount(n: int) -> int:
    i: int = 1
    factor_count: int = 0

    while i <= n:
        if n % i == 0:
            factor_count += 1
        i += 1

    return factor_count


def isPrime(n: int) -> bool:
    return factorCount(n) == 2


def primesCount(n: int) -> int:
    i: int = 1
    count: int = 0
    while i <= n:
        if isPrime(i):
            count += 1
        i += 1
    return count


n: int = int(input("Enter a number: "))

print(primesCount(n))
