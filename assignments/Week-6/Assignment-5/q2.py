def arrangeChars(s):
    charMap = dict()

    for c in s:
        if c in charMap:
            charMap[c] += 1
        else:
            charMap[c] = 1

    sorted_list = sorted(charMap.items(), key=lambda x: x[1], reverse=True)

    return "".join([k * v for k, v in sorted_list])


print(arrangeChars("aaeroplane"))
print(arrangeChars("heelllllooo"))
