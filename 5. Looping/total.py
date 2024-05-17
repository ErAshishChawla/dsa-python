"""
start, end | start < end
start to end total
"""


def total(start: int, end: int) -> int:
    result: int = 0

    i: int = start
    while i <= end:
        result += i
        i += 1
    return result


start: int = int(input("Enter the value of start: "))
end: int = int(input("Enter the value of end: "))

print(f"Addition of all numbers from {start} to {end} = {total(start, end)}")
