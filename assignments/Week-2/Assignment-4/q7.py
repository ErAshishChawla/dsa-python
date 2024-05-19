total: int = 0
count: int = 0

while True:
    num: int = int(input("Enter a number: "))
    if num == 0:
        break
    total += num
    count += 1

print(total / count)
