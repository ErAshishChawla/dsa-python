"""
string = "abc xyz pqr lmn"

output = "nml rqp zyx cba"
"""


def reverse_words(s: str):
    temp_string = s

    # Split the string into the words
    words: list[str] = temp_string.split(" ")

    # reversed words
    reversed_words: list[str] = []

    # Reverse the words
    for i in words:
        # Now i have each word, now we need to reverse it
        reversed_words.append(i[::-1])

    # Now we have reversed words, we need to reverse the list
    reversed_list = reversed_words[::-1]

    # Now we have reversed list, we need to join them
    return " ".join(reversed_list)


print(
    reverse_words(
        "abc xyz pqr lmn",
    )
)

print()
