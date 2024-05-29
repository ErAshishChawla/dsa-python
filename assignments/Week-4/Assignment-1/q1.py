import random


def sliceList(lst: list, start: int, end: int) -> list:
    slicedList = []
    for i in range(start, end):
        slicedList.append(lst[i])
    return slicedList


random_list = [random.randint(1, 100) for i in range(1, 101)]

print("Original List -> ", random_list)

start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
sliced_list = sliceList(random_list, start, end)
print(sliced_list)
