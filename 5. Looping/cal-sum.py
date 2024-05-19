"""
Continous user input until user enters 0. Calculate the sum of all numbers entered by the user
"""

total: int = 0

while True:
    num: int = int(input("Enter a number: "))
    if num == 0:
        break
    total += num

print(total)
