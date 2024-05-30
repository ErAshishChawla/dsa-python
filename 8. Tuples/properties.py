from typing import Tuple

tup: Tuple = (32, 45, 12, 78, 45, 90, 23, 45, 67, 89)

# Accessing elements of a tuple
print(tup[0])
print(tup[1])

# Traverse through a tuple
for i in tup:
    print(i, end=" ")
print()

for i in range(0, len(tup)):
    print(tup[i], end=" ")

print(tup.count(45))
print(tup.index(45))

print(40 in tup)
print(40 not in tup)

print(tup[1:4])

tup2 = tup + (4, 5, 6)
print(tup2)

tup3 = 1, 3, 5, 6, 7
print(tup3)

tup4 = (1,)
print(tup4)

tup5 = tuple(i for i in range(1, 11))
print(tup5)

print(tuple())
