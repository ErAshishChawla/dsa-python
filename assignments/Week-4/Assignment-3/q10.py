def countAlphabets(s: str) -> int:
    count = 0
    for i in s:
        if "a" <= i <= "z" or "A" <= i <= "Z":
            count += 1
    return count


input_str = input("Enter a string: ")
print(countAlphabets(input_str))
