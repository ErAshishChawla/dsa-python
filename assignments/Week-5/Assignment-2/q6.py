my_dict = {}

config = {
    "x": {
        "s": 11,
        "e": 19,
    },
    "y": {
        "s": 21,
        "e": 29,
    },
    "z": {
        "s": 31,
        "e": 39,
    },
}

for k, v in config.items():
    my_dict[k] = [i for i in range(v["s"], v["e"] + 1)]

print(
    my_dict
)  # {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19], 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29], 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

print(my_dict["x"][4])
print(my_dict["y"][4])
print(my_dict["z"][4])
