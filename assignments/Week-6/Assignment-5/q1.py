def oddCharacters(s: str) -> list[str]:
    charMap = dict()

    for c in s:
        if c in charMap:
            charMap[c] += 1
        else:
            charMap[c] = 1

    return [k for k, v in charMap.items() if v % 2 != 0]


print(oddCharacters("hello"))  # ['h', 'e', 'o']
print(oddCharacters("aeroplane"))
