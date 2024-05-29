import random


def interchangeFirstLast(lst: list) -> list:
    return lst[-1:-2:-1] + lst[1 : len(lst) - 1] + lst[0:1]


random_list = [random.randint(1, 100) for i in range(1, 11)]

print("Original List -> ", random_list)

sliced_list = interchangeFirstLast(random_list)
print(sliced_list)
