"""
Ask a string from user
Replace all vowels with z.
"""


def replace_vowels(my_string) -> str:
    vowels = "aeiouAEIOU"

    # new_list = []
    # for i in my_string:
    #     if i in vowels:
    #         new_list.append("z")
    #     else:
    #         new_list.append(i)

    # return "".join(new_list)

    return "".join(["z" if i in vowels else i for i in my_string])


my_string = input("Enter a string: ")

print(replace_vowels(my_string))
