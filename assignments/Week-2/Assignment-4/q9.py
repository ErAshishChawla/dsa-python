def isPrime(n: int) -> bool:
    i: int = 1

    if n <= 1:
        return False

    while i <= n:
        if i == 1 or i == n:
            pass
        elif n % i == 0:
            return False
        i += 1

    return True


## This is fine but the better approach is counting the factor numbers, then you dont have to deal with the edge cases

print(isPrime(97))
print(isPrime(1))
print(isPrime(0))
print(isPrime(4))
