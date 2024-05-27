"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1  
"""


def pattern(n: int) -> None:
    if n % 2 != 0:
        for i in range(1, (n // 2 + 1) + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
        for i in range(1, n // 2 + 1):
            for j in range((n // 2 + 1) - i, 0, -1):
                print(j, end=" ")
            print()


pattern(11)
