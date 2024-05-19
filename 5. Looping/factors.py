def factors(n1: int) -> int:
    i: int = 1
    count: int = 0

    while i <= n1:
        if n1 % i == 0:
            count += 1
            # print(i, end=" ")
        i += 1
    # print()
    return count


def isPrime(n: int) -> bool:
    return factors(n) == 2


print(isPrime(7))
