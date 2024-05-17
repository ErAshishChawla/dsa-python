"""
start to end how many even numbers
"""


def count_even(start: int, end: int) -> int:
    result: int = 0

    i: int = start
    while i <= end:
        if i % 2 == 0:
            result += 1
        i += 1
    return result


start: int = int(input("Enter the value of start: "))
end: int = int(input("Enter the value of end: "))

print(f"Total even numbers from {start} to {end} = {count_even(start, end)}")
