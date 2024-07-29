my_dict = {
    "physics": 78,
    "chemistry": 11,
    "maths": 79,
}

max_marks = 0
for v in my_dict.values():
    if v > max_marks:
        max_marks = v
print(max_marks)
