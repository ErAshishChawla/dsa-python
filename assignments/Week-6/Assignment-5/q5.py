def capitalizeFirstAndLastLetter(s):
    words = s.split()
    converted_words = []

    for word in words:
        if len(word) == 1:
            converted_words.append(word.upper())
        else:
            converted_words.append(word[0].upper() + word[1:-1] + word[-1].upper())

    return " ".join(converted_words)


print(capitalizeFirstAndLastLetter("hello world"))  # Hello world
print(capitalizeFirstAndLastLetter("python is a great language"))  # Hello world
