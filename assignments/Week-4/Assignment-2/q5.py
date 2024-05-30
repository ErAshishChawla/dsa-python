def result(num: int) -> list:
    return len([i for i in range(1, num + 1) if i % 3 == 0 and i % 6 == 0])


print(result(1000))
