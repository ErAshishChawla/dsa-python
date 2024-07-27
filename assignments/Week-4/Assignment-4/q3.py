def reverseWords(s: str) -> str:
    return " ".join([i for i in s.split()[::-1]])


print(reverseWords("python is great"))
