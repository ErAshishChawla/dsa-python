"""
Ask a string from user

# reverse the words in a string
"""


def reverse_words_string(my_string: str) -> str:
    result: list[str] = (
        my_string.split()
    )  # this will give us all the words in the string

    return " ".join([i[::-1] for i in result])


my_string = input("Enter a string: ")
print(reverse_words_string(my_string))
