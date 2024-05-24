def reverse(n: int) -> int:
    rev: int = 0
    num: int = n
    while num > 0:
        last_digit = num % 10
        rev = rev * 10 + last_digit
        num = num // 10
    return rev


def checkPalindrome(n: int) -> bool:
    return n == reverse(n)


print(checkPalindrome(91))
print(checkPalindrome(1221))
print(checkPalindrome(9854))
print(checkPalindrome(123454321))
