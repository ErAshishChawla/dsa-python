a = [1, 2, 3, 4, 5]

# Sum of even numbers
total = 0
for i in a:
    if i % 2 == 0:
        total = total + i
print("Total: ", total)

# Sum of numbers at even positions

total = 0
for i in range(0, len(a), 2):
    total = total + a[i]
print("Total: ", total)

total = 0
for i in range(0, len(a)):
    if i % 2 == 0:
        total = total + a[i]
print("Total: ", total)
