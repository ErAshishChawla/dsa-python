def countNonAlphabets(s: str) -> int:
    count = 0
    for i in s:
        if not ("a" <= i <= "z" or "A" <= i <= "Z"):
            count += 1
    return count


print(countNonAlphabets("abc%$#gyhy"))
print(countNonAlphabets("AB788&*(^%&*%^&aaaa"))
print(countNonAlphabets("1233^&*(*      0000011"))
print(countNonAlphabets("abcdABCD"))
