def pattern(n: int) -> None:
    i: int = 1

    while i <= n:
        print(i * 10, end=" ")
        i += 1

    print()


pattern(4)
pattern(11)
