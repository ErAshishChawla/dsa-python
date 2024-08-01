def rotateStr(s, n):
    rotations = n % len(s)
    return s[-rotations:] + s[: len(s) - rotations]


def rotateStr2(s, n):
    temp_string = s
    for _ in range(n):
        temp_string = temp_string[-1] + temp_string[:-1]
    return temp_string


print(rotateStr("abcdef", 4))
print(rotateStr2("abcdef", 4))
