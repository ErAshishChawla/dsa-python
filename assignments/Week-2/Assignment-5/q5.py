def addDigits(n: int) -> int:
    total: int = 0
    num: int = n

    while num > 0:
        last_digit = num % 10
        total += last_digit
        num = num // 10

    return total


print(addDigits(123))
print(addDigits(58714))
