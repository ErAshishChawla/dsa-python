def sumOfdigits(num: int) -> bool:
    total = 0
    temp = num
    while temp > 0:
        last_digit = temp % 10
        total += last_digit
        temp = temp // 10
    return total


def result(num: int) -> list:
    return [i for i in range(1, num + 1) if i % sumOfdigits(i) == 0]


print(result(1000))
