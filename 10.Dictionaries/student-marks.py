students = {
    "anirudh": {
        "physics": 54,
        "maths": 11,
        "english": 99,
        "history": 43,
    },
    "sanjay": {
        "physics": 13,
        "maths": 40,
    },
    "vandana": {
        "physics": 65,
        "maths": 85,
        "english": 94,
    },
}

# Q1
for student, marks in students.items():
    total = 0
    for mark in marks.values():
        total += mark
    print(f"{student} has scored {total} marks.")

# Q2
for student, marks in students.items():
    total = 0
    for mark in marks.values():
        total += mark
    percentage = (total / (len(marks) * 100)) * 100
    print(f"{student} has scored {percentage:.2f}%")
