import random


def split_half(lst: list) -> list:
    half = len(lst) // 2
    print("First half -> ", lst[:half])
    print("First half -> ", lst[half:])


random_list = [random.randint(1, 100) for i in range(1, 11)]

print("Original List -> ", random_list)

sliced_list = split_half(random_list)
print(sliced_list)
