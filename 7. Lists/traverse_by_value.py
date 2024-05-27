# Traverse by value

a = [1, 2, 3, 4, 5]

for i in a:
    print(i, end=" ")
print()

# Traverse by both index/value
for index, value in enumerate(a):
    print(index, value)
