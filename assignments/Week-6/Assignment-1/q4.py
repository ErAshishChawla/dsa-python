student_data = [
    {"Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]}},
    {"Max": {"age": 22, "marks": [79, 85, 88, 90, 87]}},
    {"Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]}},
    {"Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]}},
    {"Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]}},
    {"Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]}},
    {"Olivia": {"age": 24, "marks": [82, 86, 90, 87, 84]}},
]


def sorter(x):
    total = 0
    for k, v in x.items():
        total = sum(v["marks"])
    return total


sorted_student_data = sorted(student_data, key=sorter)

for i in sorted_student_data:
    for k, v in i.items():
        print(f"{k} has socred {sum(v['marks'])}")
