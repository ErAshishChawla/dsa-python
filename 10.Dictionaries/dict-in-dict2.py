students = {
    "anirudh": {
        "age": 66,
        "gender": "Male",
        "marks": [2, 3, 11, 24, 55],
    },
    "sanjay": {
        "age": 11,
        "gender": "Male",
        "marks": [54, 76, 12, 232, 1, 65],
    },
    "vandana": {
        "age": 53,
        "gender": "Female",
        "marks": [65, 77, 33],
    },
}


def sortDict(x):
    total = 0
    values = x[1]
    if "marks" in values:
        for i in values["marks"]:
            total += i
    return total


x = dict(sorted(students.items(), key=sortDict))

print(x)
