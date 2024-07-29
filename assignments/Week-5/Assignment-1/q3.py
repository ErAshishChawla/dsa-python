my_dict = {
    "physics": 78,
    "chemistry": 11,
    "maths": 79,
}

passing_marks = 33
for k, v in my_dict.items():
    if v > 33:
        print(k, v)
