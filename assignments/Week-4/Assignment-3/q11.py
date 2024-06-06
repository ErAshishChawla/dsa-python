def countSpaces(s: str) -> int:
    count = 0
    for i in s:
        if i == " ":
            count += 1

    return count


input_str = input("Enter a string: ")
print(countSpaces(input_str))
