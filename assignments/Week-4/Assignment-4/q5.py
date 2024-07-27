def reverseWords(s: str) -> str:
    return " ".join([i[::-1] for i in s.split()])


print(reverseWords("python is great"))  # nohtyp si taerg
