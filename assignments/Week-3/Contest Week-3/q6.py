def pattern(n: int) -> None:
    top_half = n // 2 + 1
    bottom_half = n - top_half

    for i in range(top_half, 0, -1):
        for j in range(1, top_half - i + 1):
            print(" ", end=" ")
        for k in range(1, (2 * i - 1) + 1):
            if k % 2 == 0:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()
    for i in range(1, bottom_half + 1):
        for j in range(1, bottom_half - i + 1):
            print(" ", end=" ")
        for k in range(1, (2 * i + 1) + 1):
            if k % 2 == 0:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()


pattern(7)
