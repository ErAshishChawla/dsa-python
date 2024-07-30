from copy import deepcopy

my_dict = {"anirudh": 78, "akul": 11, "muskan": 79, "anirudh": 99, 11: 78}

new_dict = my_dict.copy()
print(new_dict)

deep_new_dict = deepcopy(new_dict)
