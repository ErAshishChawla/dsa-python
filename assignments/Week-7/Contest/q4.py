from typing import List


def highestSubarraySum(arr: List[List[int]]) -> int:
    max_sum = 0
    for sub_arr in arr:
        sum_sub_arr = sum(sub_arr)
        if sum_sub_arr > max_sum:
            max_sum = sum_sub_arr
    return max_sum


my_list = [[1, 2, 1, 6, 2], [5, 6, 5], [-1, 1, 1, 1, 1]]
print(highestSubarraySum(my_list))  # 10
