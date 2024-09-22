def extractDigits(n: int):
    temp_num = n
    digits = []
    while temp_num > 0:
        digit = temp_num % 10
        temp_num //= 10
        digits.append(digit)

    return digits


def sumOfOddAndEvenPositionDigits(n: int):
    digits = extractDigits(n)
    odd_sum = 0
    even_sum = 0
    for i in range(len(digits)):
        if i % 2 == 0:
            even_sum += digits[i]
        else:
            odd_sum += digits[i]

    return odd_sum, even_sum


n = 1212112
odd_sum, even_sum = sumOfOddAndEvenPositionDigits(n)

if odd_sum == even_sum:
    print("Yes")
else:
    print("No")
