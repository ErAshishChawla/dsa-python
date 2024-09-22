def removeDuplicateWords(s: str):
    words = s.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return " ".join(unique_words)


s = "Python is great and Java is also great"
print(removeDuplicateWords(s))  # Python is great and Java also
