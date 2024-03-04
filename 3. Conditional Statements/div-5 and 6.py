"""
Ask a number. Print YES if it is divisible by 5 and 6 otherwise NO
"""

number: int = int(input("Enter a number= "))

if number % 5 == 0 and number % 6 == 0:
    print("YES")
else:
    print("NO")
