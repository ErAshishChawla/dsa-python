a = [78, 67, 44, -100, 87, 33, 31]

for i in range(0, len(a)):
    print(a[i], end=" ")
print()

# Printing even indexes:
for i in range(0, len(a), 2):
    print(a[i], end=" ")
print()

# Printing using negative indexes:
# This also reverses the list
for i in range(-1, -len(a) - 1, -1):
    print(a[i], end=" ")
print()

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")
print()
