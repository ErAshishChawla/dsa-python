def countFactors(n: int) -> int:
    count: int = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def checkPrime(n: int) -> None:
    if countFactors(n) == 2:
        print("YES")
    else:
        print("NO")


checkPrime(2)
checkPrime(97)
checkPrime(100)
checkPrime(1)
checkPrime(0)
