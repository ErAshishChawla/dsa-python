def smallest_number(num1: int, num2: int, num3: int, num4: int):
    min_num: int = num1

    if num2 < min_num:
        min_num = num2
    elif num3 < min_num:
        min_num = num3
    elif num4 < min_num:
        min_num = num4

    print(f"The smallest number is {min_num}")


num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))
num3: int = int(input("Enter the third number: "))
num4: int = int(input("Enter the fourth number: "))

min_num: int = num1

smallest_number(num1, num2, num3, num4)
