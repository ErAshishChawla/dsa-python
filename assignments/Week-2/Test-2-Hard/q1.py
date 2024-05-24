def reverse(n: int) -> int:
    rev: int = 0

    num: int = n
    while num > 0:
        last_digit: int = num % 10
        rev = rev * 10 + last_digit
        num = num // 10
    return rev


print(reverse(91))
print(reverse(1000))
print(reverse(1474))
