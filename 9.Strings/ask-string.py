"""
Continuously ask a string from user. If the string is 'q or Q', then stop asking.
Then print whatever user has entered.
"""


def ask_string():
    input_str: list[str] = []

    while True:
        s = input("Enter a string: ")

        if s.lower() == "q":
            break

        input_str.append(s)

    for i in input_str:
        print(i)


ask_string()
