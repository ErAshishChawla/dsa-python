a: list = [78, 67, 44, -100, 87, 33, 31]
print(a)

# This will completely replace the list with value. Changing data type
# a = 100
# print(a)

# a[0] = 100
# a[-1] = 100
# print(a)

#
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        a[i] = a[i] + 1
    else:
        a[i] = a[i] - 1
print(a)

for i in range(0, len(a)):
    if i % 2 == 0:
        a[i] = a[i] + 1
    else:
        a[i] = a[i] - 1
print(a)
