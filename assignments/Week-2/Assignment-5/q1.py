def pattern(n: int) -> None:
    num = 2
    for i in range(1, n + 1):
        print(num, end=" ")
        num = num * 10 + 2


pattern(6)
