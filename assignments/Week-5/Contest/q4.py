from typing import Dict


def countWords(s: str) -> Dict:
    char_hash = dict()

    words = s.split(" ")

    for i in words:
        if i in char_hash:
            char_hash[i] = char_hash[i] + 1
        else:
            char_hash[i] = 1
    return char_hash


print(countWords("The sun is shining and the weather is nice"))
print(countWords("The cat and the dog played in the park The cat chased the dog"))
