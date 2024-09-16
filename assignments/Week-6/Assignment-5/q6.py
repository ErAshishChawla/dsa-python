def result(s):
    charMap = dict()
    for c in s:
        if c in charMap:
            charMap[c] += 1
        else:
            charMap[c] = 1

    singles = [k for k, v in charMap.items() if v == 1]
    multiples = [k for k, v in charMap.items() if v > 1]

    print(f'string1 = {"".join(singles)}')
    print(f'string2 = {"".join(multiples)}')


result("aabbcceffgh")
