def divs(n1: int, n2: int) -> int:
    count: int = 0

    i: int = 1

    while i <= n1:
        if i % n2 == 0:
            count += 1
        i += 1
