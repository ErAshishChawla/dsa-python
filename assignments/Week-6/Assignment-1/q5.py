student_data = [
    [78, 92, 85, "Alice"],
    [82, 79, 81, "Bob"],
    [92, 88, 85, "Charlie"],
    [80, 79, 82, "Diana"],
    [92, 85, 90, "Eva"],
    [85, 80, 86, "Frank"],
    [87, 92, 88, "Gina"],
]

sorted_student_data = sorted(student_data, key=lambda x: sum(x[:3]))

for i in sorted_student_data:
    print(f"{i[3]} has scored {sum(i[:3])} marks")
