def result(num: int) -> list:
    return [2**i for i in range(0, num) if 2**i < num]


print(result(10))
