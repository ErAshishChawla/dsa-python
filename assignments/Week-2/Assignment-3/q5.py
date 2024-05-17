def printPattern(n: int) -> None:
    # Assuming n > 0
    start: int = -1 * n
    end: int = n

    # if n<0
    if n < 0:
        start = n
        end = -1 * n

    while start <= end:
        print(start, end=" ")
        start += 1
    print()


printPattern(5)
printPattern(-9)
