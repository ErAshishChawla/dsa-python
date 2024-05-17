"""
Ask M and N from the user and print all the numbers between M to N (including M and N)
"""


def print_m_to_n(m: int, n: int) -> None:
    lower: int = m
    upper: int = n

    # Swap the values of lower and upper if lower is greater than upper
    if upper < lower:
        temp = lower
        lower = upper
        upper = temp

    # Print all the numbers between lower and upper
    while lower <= upper:
        print(lower, end=" ")
        lower += 1

    print()


m: int = int(input("Enter the value of m: "))
n: int = int(input("Enter the value of n: "))

print_m_to_n(m, n)
