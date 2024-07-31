add = lambda a, b: a + b
print(add(2, 3))  # 5

mul = lambda a, b, c: a * b * c if a != 0 and b != 0 and c != 0 else "Invalid"
print(mul(2, 3, 4))  # 24

lst = lambda n: [i for i in range(1, n + 1)]
print(lst(5))  # [1, 2, 3, 4, 5]
