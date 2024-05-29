import random


def last_n_elements(lst: list, n: int) -> list:
    return lst[-n:]


random_list = [random.randint(1, 100) for i in range(1, 101)]

print("Original List -> ", random_list)

n = int(input("Enter the number of elements to slice: "))

sliced_list = last_n_elements(random_list, n)
print(sliced_list)
