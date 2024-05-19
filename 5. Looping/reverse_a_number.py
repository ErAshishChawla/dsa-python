def reverseANumber(n: int) -> int:
    reverse: int = 0

    i = n  # Just to retain the original value of n
    if n < 0:
        i = (
            -1 * n
        )  # Dealing with negative numbers. This makes the number positive. We will return the negative number at the end if the input number was negative

    while i > 0:
        lastDigit = i % 10  # Extracting the last digit
        reverse = (
            reverse * 10 + lastDigit
        )  # Appending the last digit to the reverse number
        i = i // 10  # Removing the last digit from the number

    return -1 * reverse if n < 0 else reverse


print(reverseANumber(-1347))  # 54321
