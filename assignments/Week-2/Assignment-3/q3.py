def multiplicationTable(n: int) -> None:
    i: int = 1
    while i <= 10:
        print(f"{n} X {i} = {n*i}")
        i += 1
    print()


multiplicationTable(13)
multiplicationTable(231)
