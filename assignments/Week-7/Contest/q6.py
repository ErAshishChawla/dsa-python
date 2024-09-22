from typing import List


def sumOfDigits(n: int) -> int:
    temp_num = n
    sum_of_digits = 0
    while temp_num > 0:
        # Extract last digit
        last_digit = temp_num % 10
        # Remove last digit
        temp_num = temp_num // 10

        sum_of_digits += last_digit
    return sum_of_digits


def sumOfDigitsOfList(arr: List[int]) -> List[int]:
    sum_of_digits = []
    for num in arr:
        sum_of_digits.append(sumOfDigits(num))
    return sum_of_digits


my_list = [12, 67, 98, 34]
print(sumOfDigitsOfList(my_list))  # 25
