def factorial(num: int) -> int:
    fact = 1
    for i in range(1, num):
        fact = fact * i
    return fact


def result(num: int) -> list:
    return [factorial(i) for i in range(1, num) if factorial(i) < num]


print(result(1000))
