"""
Ask a number from user.
Print positive, negaitive or zero based on the number.
"""

num: int = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")


if num > 0:
    print("Positive")
else:
    if num == 0:
        print("Zero")
    else:
        print("Negative")
