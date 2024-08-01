def joinStr(lst, sep):
    final_str = ""
    for i in lst:
        final_str = final_str + i + sep

    return final_str


n = ["Hello", "World", "Python"]

print(joinStr(n, " "))
