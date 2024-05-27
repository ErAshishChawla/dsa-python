import copy

a = [56, 32, "Akul", "Ambani", False, [1, 2, 3], 11.112]
b = copy.copy(a)  # shallow copy

print("A -> ", a)
print("B -> ", b)

a.append(100)
print("A -> ", a)
print("B -> ", b)

print("A internal list id-> ", id(a[5]))
print("B internal list id-> ", id(b[5]))

a[5].append(4)
print("A -> ", a)
print("B -> ", b)

c = copy.deepcopy(a)  # deep copy
print("C -> ", c)

a[5].append(5)
print("A -> ", a)
print("C -> ", c)
