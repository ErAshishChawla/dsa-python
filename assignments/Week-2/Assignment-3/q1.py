def div_by_3_and_5(start: int, end: int) -> None:
    i: int = start

    while i <= end:
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
        i += 1
    print()


div_by_3_and_5(10, 30)
div_by_3_and_5(1, 60)
