"""
Ask number from user. Print positive negative or zero
"""

number: int = int(input("Enter a number= "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
