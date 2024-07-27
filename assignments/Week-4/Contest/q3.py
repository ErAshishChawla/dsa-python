def removeDuplicates(s: str) -> str:
    unique = ""

    for i in s:
        if i not in unique:
            unique += i
    return unique


print(removeDuplicates("Hello"))
