def rotateLeft(s: str, d: int) -> str:
    if d == 0:
        return s
    elif d > len(s):
        d = d % len(s)

    return s[d:] + s[:d]


def rotateRight(s: str, d: int) -> str:
    if d == 0:
        return s
    elif d > len(s):
        d = d % len(s)

    return s[-d:] + s[: len(s) - d]


s = "pythonprogramming"
d = 4
print(rotateLeft(s, d))  # onprogrammingpyth
print(rotateRight(s, d))  # mingpythonprogram
