def isPrime(num: int) -> bool:
    factors_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors_count += 1
    return factors_count == 2


def result(num: int) -> list:
    return [i for i in range(1, num + 1) if isPrime(i)]


print(result(500))
