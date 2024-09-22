import unittest
from typing import List


def secondLargest(arr: List[float]):
    if len(arr) < 2:
        return -1

    largest_num_idx = 0
    second_largest_num_idx = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[largest_num_idx]:
            second_largest_num_idx = largest_num_idx
            largest_num_idx = i
        elif arr[i] > arr[second_largest_num_idx] and arr[i] != arr[largest_num_idx]:
            second_largest_num_idx = i

    return (
        -1
        if arr[second_largest_num_idx] == arr[largest_num_idx]
        else arr[second_largest_num_idx]
    )


class TestSecondLargest(unittest.TestCase):
    def test_distinct_elements(self):
        self.assertEqual(secondLargest([1, 2, 3, 4, 5]), 4)

    def test_duplicate_elements(self):
        self.assertEqual(secondLargest([1, 2, 3, 3, 4, 5, 5]), 4)

    def test_all_elements_same(self):
        self.assertEqual(secondLargest([5, 5, 5, 5]), -1)

    def test_single_element(self):
        self.assertEqual(secondLargest([1]), -1)

    def test_empty_list(self):
        self.assertEqual(secondLargest([]), -1)

    def test_negative_numbers(self):
        self.assertEqual(secondLargest([-10, -20, -30, -40, -50]), -20)

    def test_floating_point_numbers(self):
        self.assertEqual(secondLargest([1.1, 2.2, 3.3, 4.4, 5.5]), 4.4)


unittest.main()
