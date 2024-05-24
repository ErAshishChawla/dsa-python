def reverse(n: int) -> int:
    rev: int = 0
    num: int = n
    while num > 0:
        last_digit = num % 10
        rev = rev * 10 + last_digit
        num = num // 10
    return rev


def printWords(n: int) -> None:
    words = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
    ]
    rev = reverse(n)

    while rev > 0:
        last_digit = rev % 10
        print(words[last_digit], end=" ")
        rev = rev // 10
    print()


printWords(91)
printWords(1221)
printWords(9854)
printWords(1001)
