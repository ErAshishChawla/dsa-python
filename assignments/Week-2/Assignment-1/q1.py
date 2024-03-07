def maxi(num1: int, num2: int, num3: int):
    max_num = num1

    if num2 > max_num:
        max_num = num2
    elif num3 > max_num:
        max_num = num3

    print(max_num)


def mini(num1: int, num2: int, num3: int):
    min_num = num1

    if num2 < min_num:
        min_num = num2
    elif num3 < min_num:
        min_num = num3

    print(min_num)


maxi(10, -20, 30)
mini(-100, -1, 20)
