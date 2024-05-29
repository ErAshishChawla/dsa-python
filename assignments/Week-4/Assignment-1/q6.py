import random


def reverse_list(lst: list) -> list:
    # sliced_list = lst[-n:]
    # return sliced_list[::-1]

    return lst[::-1]


random_list = [random.randint(1, 100) for i in range(1, 101)]

print("Original List -> ", random_list)

sliced_list = reverse_list(random_list)
print(sliced_list)
