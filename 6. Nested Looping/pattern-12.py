"""
@ @ @ @ * @ @ @ @
@ @ @ * * * @ @ @
@ @ * * * * * @ @
@ * * * * * * * @
* * * * * * * * *
"""

n = 7

for i in range(1, n + 1):
    # First loop to deal with first half of the pattern
    for j in range(i, n):
        print(" ", end=" ")

    # Second loop to deal with second half of the pattern
    for k in range(1, (2 * i - 1) + 1):
        print("*", end=" ")

    print()
