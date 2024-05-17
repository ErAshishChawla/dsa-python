def middle(num1: int, num2: int, num3: int) -> int:
    if num1 <= num2 <= num3 or num3 <= num2 <= num1:
        return num2
    elif num1 <= num3 <= num2 or num2 <= num3 <= num1:
        return num3
    else:
        return num1


def checkDivisibility(dividend: float, divisor: int) -> bool:
    return dividend % divisor == 0


num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))
num3: int = int(input("Enter the third number: "))

middle_num = middle(num1, num2, num3)
print(middle_num)

if checkDivisibility(middle_num, 3) and checkDivisibility(middle_num, 4):
    print(f"{middle_num} is divisible by both {3} and {4}")
else:
    print(f"{middle_num} is not divisible by both {3} and {4}")
