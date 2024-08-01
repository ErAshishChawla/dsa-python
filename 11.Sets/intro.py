a = {33, 34, 11, 33, 333, 33, 33, "ANirudh", "abc", 99.9}
b = {33, 12, 1, 9, 5, 6}


print(a)
a.add(199)
print(a)
a.remove(333)
print(a)

for i in a:
    print(i, end=" ")

print(a.union(b))
print(a.intersection(b))
