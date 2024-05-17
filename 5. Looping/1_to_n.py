def print_1_to_n(n: int) -> None:
    i: int = 1

    while i <= n:
        print(i, end=" ")
        i += 1
    print()


# n: int = int(input("Enter the value of n: "))

print_1_to_n(10)
print_1_to_n(15)
