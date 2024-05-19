number: int = int(input("Enter a number: "))

total: int = 0

i = number

while i > 0:
    total += i % 10
    i = i // 10

print(total)
