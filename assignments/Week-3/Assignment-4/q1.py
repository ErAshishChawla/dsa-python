def even_odd(lst: list[int]) -> list[list[int]]:
    even = []
    odd = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [even, odd]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original List:", a)
print("Even List:", even_odd(a)[0])
print("Odd List:", even_odd(a)[1])
