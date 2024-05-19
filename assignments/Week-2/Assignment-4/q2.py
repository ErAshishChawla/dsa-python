"""
Condition for leap year

1. If the year is evenly divisible by 4, then it is likely a leap year.(step 3)
2. If the year is not divisible by 4, then it is not a leap year.

3. If the year is divisible by 4, but not by 100, then it is a leap year
4. If the year is divisible by 100, then it is likely not a leap year.(step 5)

5. If the year is divisible by 100, but not by 400, then it is not a leap year
6. If the year is divisible by 400, then it is a leap year.
"""

start: int = 1
end: int = 2000

while start <= end:
    # if start % 4 == 0:
    #     if start % 100 != 0:
    #         count += 1
    #         print(start)
    #     else:
    #         if start % 400 == 0:
    #             count += 1
    #             print(start)

    if start % 400 == 0:
        print(start)
    elif start % 100 != 0 and start % 4 == 0:
        print(start)

    start += 1
