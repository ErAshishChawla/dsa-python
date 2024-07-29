my_dict = {
    "physics": 78,
    "chemistry": 11,
    "maths": 79,
}

max_marks = 0
subject = ""
for k, v in my_dict.items():
    if v > max_marks:
        max_marks = v
        subject = k
print(subject, max_marks)
