"""
print the following pattern:
1 11 101 1001 10001 100001
"""


def pattern(n: int) -> None:
    i: int = 1
    # multiplier: int = 10
    # start = 1
    # result: int = 1

    # while i <= n:
    #     print(result, end=" ")
    #     result = start * multiplier + start
    #     multiplier *= 10
    #     i += 1

    num: int = 1
    while i <= n:
        print(num, end=" ")
        num = 10**i + 1
        i += 1


pattern(6)
