def average(num1: float, num2: float, num3: float) -> float:
    return (num1 + num2 + num3 + num4) / 3


def isFirstGreater(num1: float, num2: float) -> bool:
    if num1 > num2:
        return True
    return False


num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))
num3: float = float(input("Enter the third number: "))
num4: float = float(input("Enter the fourth number: "))

average_num: float = average(num1, num2, num3)
print(f"The average of {num1}, {num2}, {num3} is: {average_num}")


if isFirstGreater(average_num, num4):
    print(f"The average is the greater than {num4}")
else:
    print(f"The average is less than {num4}")
