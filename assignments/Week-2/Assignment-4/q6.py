num: int = int(input("Enter a number: "))

i: int = 1
start: int = 1

while i <= num:
    print(start, end=" ")
    start = (start * 10) + 1
    i += 1
