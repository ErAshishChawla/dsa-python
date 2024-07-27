def printWordsLargerThanK(s: str, k: int) -> str:
    temp_string_words = []
    for i in s.split(" "):
        if len(i) >= k:
            temp_string_words.append(i)

    return " ".join(temp_string_words)


print(
    printWordsLargerThanK("python is a great language. Very easy to understand also", 5)
)
