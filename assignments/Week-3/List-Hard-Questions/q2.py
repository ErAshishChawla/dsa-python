from typing import List


def mergeTwoSortedLists(l1: list, l2: list) -> list:
    l1_len = len(l1)
    l2_len = len(l2)

    l1_index = 0
    l2_index = 0

    merged_list = []

    while True:
        if l1_index == l1_len:
            for i in range(l2_index, l2_len):
                merged_list.append(l2[i])
            break
        if l2_index == l2_len:
            for i in range(l1_index, l1_len):
                merged_list.append(l1[i])
            break

        if l1[l1_index] < l2[l2_index]:
            merged_list.append(l1[l1_index])
            l1_index += 1
        else:
            merged_list.append(l2[l2_index])
            l2_index += 1

    return merged_list


l1 = [1, 2, 3, 4]
l2 = [-1, 0, 1, 2, 3, 4, 5, 6]

print(mergeTwoSortedLists(l1, l2))
