numberList = []

for i in range(1, 6):
    num = int(input(f"Enter number {i}: "))
    numberList.append(num)

char = input("Enter a character: ")

result = char.join([str(i) for i in numberList])
print(result)
