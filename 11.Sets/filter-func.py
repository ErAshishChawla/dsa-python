def filterFn(x):
    return x % 2 == 0


b = filter(filterFn, [1, 2, 3, 4, 5])
print(b)
print(list(b))
