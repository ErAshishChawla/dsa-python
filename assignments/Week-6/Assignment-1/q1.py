from typing import Dict, List


def total(l: List[int]) -> int:
    total = 0
    for i in l:
        total += i
    return total


def totat_marks(student_data: Dict[str, List[int]]) -> None:
    new_dict = dict(sorted(student_data.items(), key=lambda x: total(x[1])))

    for k, v in new_dict.items():
        print(f"{k} has scored {total(v)} marks")


student_data = {
    "Alice": [85, 90, 88, 92, 89],
    "Bob": [78, 82, 79, 81, 80],
    "Charlie": [92, 95, 88, 85, 91],
    "Diana": [76, 80, 79, 82, 85],
    "Eva": [88, 92, 85, 90, 87],
    "Frank": [83, 85, 80, 86, 88],
    "Gina": [90, 87, 92, 88, 86],
}

totat_marks(student_data)
