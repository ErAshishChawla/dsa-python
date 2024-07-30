students = {
    "anirudh": [54, 6, 21, 5, 66],
    "sagar": [54, 6, 21, 5, 66],
    "akul": [54, 6, 21, 5, 66],
}

for k, v in students.items():
    total = 0
    for i in v:
        total = total + i
    print(f"{k} has scored {total} marks.")
