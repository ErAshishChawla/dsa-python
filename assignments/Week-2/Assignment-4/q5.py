def pattern(n: int) -> None:
    i: int = 0

    while i <= n - 1:
        print(2**i, end=" ")
        i += 1
    print()


pattern(4)
pattern(7)
