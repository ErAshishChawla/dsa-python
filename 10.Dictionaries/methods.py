my_dict = {"anirudh": 78, "akul": 11, "muskan": 79, "anirudh": 99, 11: 78}

my_dict.update()


print(my_dict.get("anirudh"))
print(my_dict.get(11))

if "anirudh" in my_dict:
    print(my_dict["anirudh"])

if "anirudhhh" in my_dict:
    print(my_dict["anirudhhh"])


print(my_dict)
my_dict.clear()
print(my_dict)
# del my_dict
# print(my_dict)  # NameError: name 'my_dict' is not defined
