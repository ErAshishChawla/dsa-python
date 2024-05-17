"""
Ask a number from user = 50
print all the numbers from -50 to 50

Ask a number from user = 10
print all the numbers from -10 to 10

Ask a number from user = -13
print all the numbers from 13 to -13
"""


def negative(n: int) -> None:

    # if n is negative, start from -n to n
    if n < 0:
        start: int = -1 * n  # will be positive
        end: int = n  # will be negative

        # So, we need to go from positive to negative
        while start >= end:
            print(start, end=" ")
            start -= 1

    else:
        # if n is positive, start from -n to n
        start: int = -1 * n  # will be negative
        end: int = n  # will be positive

        # So, we need to go from negative to positive
        while start <= end:
            print(start, end=" ")
            start += 1


n: int = int(input("Enter a number: "))

negative(n)
