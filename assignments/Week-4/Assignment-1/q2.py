import random


def sliceList(lst: list, start: int, end: int) -> list:
    return lst[start:end]


random_list = [random.randint(1, 100) for i in range(1, 101)]

print("Original List -> ", random_list)

start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
sliced_list = sliceList(random_list, start, end)
print(sliced_list)
