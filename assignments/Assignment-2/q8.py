"""
Conditions for a leap year:

year % 4 == 0 (leap year)
year %4 == 0 and year %100 == 0 (not a leap year)
year % 4 == 0 and year % 400 == 0 (leap year)
"""

year: int = int(input("Enter a year: "))

if year <= 0:
    print("Invalid year")
elif year % 4 == 0 and year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
