def isArmstrong(n: int) -> bool:
    temp = n
    sum = 0
    while temp > 0:
        last_digit = temp % 10
        sum = sum + last_digit**3
        temp = temp // 10
    return sum == n


def armstrongRange(n1: int, n2: int) -> None:
    for i in range(n1, n2 + 1):
        if isArmstrong(i):
            print(i, end=" ")
    print()


armstrongRange(56, 1000)
