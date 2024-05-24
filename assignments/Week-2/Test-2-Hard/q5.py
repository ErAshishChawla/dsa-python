def sumOfFirstAndLastDigit(n: int) -> int:
    last_digit = n % 10
    first_digit: int = 0
    num: int = n
    while num // 10 > 0:
        num = num // 10
        first_digit = num

    return first_digit + last_digit


print(sumOfFirstAndLastDigit(1234))
print(sumOfFirstAndLastDigit(8471))
print(sumOfFirstAndLastDigit(5))
print(sumOfFirstAndLastDigit(99))
