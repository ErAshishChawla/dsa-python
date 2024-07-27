"""
Replace a char in a string
"""


def replaceChar(s: str, old: str, new: str) -> str:
    temp_string = s

    if old == new:
        return s

    return temp_string.replace(old, new)


print(replaceChar("delhi is a clean city", "i", "z"))


def replaceCharManual(s: str, old: str, new: str) -> str:
    temp_string = ""

    for i in s:
        if i.lower() == old:
            temp_string += new
        else:
            temp_string += i
    return temp_string


print(replaceCharManual("delhi is a clean city", "i", "z"))
