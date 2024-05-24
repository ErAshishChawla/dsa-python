def checkArmstrong(num: int) -> bool:
    # get the number of digits in the number
    digit_count: int = 0

    n: int = num
    while n > 0:
        n = n // 10
        digit_count += 1

    # Now as we have the count of the digits, now we will go over again to get the sum of the (digits)^digit_count
    total: int = 0
    n = num
    while n > 0:
        last_digit = n % 10
        total = total + (last_digit**digit_count)
        n = n // 10

    return total == num


print(checkArmstrong(153))
print(checkArmstrong(407))
