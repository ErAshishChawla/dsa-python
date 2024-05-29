import random


def sliceAndReverse(lst: list, start: int, end: int) -> list:
    sliced_list = lst[start:end]

    return sliced_list[::-1]


random_list = [random.randint(1, 100) for i in range(1, 101)]

print("Original List -> ", random_list)

start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
sliced_list = sliceAndReverse(random_list, start, end)
print(sliced_list)
