my_dict = {
    "anirudh": 78,
    "akul": 11,
    "muskan": 79,
}

# Generally used
for k in my_dict:
    print(k, my_dict[k])

# Also used
for k in my_dict.keys():
    print(k, my_dict[k])

# Also used
for v in my_dict.values():
    print(v)

# Also used
for k, v in my_dict.items():
    print(k, v)
