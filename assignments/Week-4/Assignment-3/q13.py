def countSmallAlphabets(s: str) -> int:
    count = 0
    for i in s:
        if "a" <= i <= "z":
            count += 1
    return count


def countCapitalAlphabets(s: str) -> int:
    count = 0
    for i in s:
        if "A" <= i <= "Z":
            count += 1
    return count


def countSpaces(s: str) -> int:
    count = 0
    for i in s:
        if i == " ":
            count += 1
    return count


def countDigits(s: str) -> int:
    count = 0
    for i in s:
        if "0" <= i <= "9":
            count += 1
    return count


def displayCounts(s: str) -> None:
    small_alphabets = countSmallAlphabets(s)
    capital_alphabets = countCapitalAlphabets(s)
    spaces = countSpaces(s)
    digits = countDigits(s)
    special_characters = len(s) - small_alphabets - capital_alphabets - spaces - digits

    print(f"Small Alphabets: {small_alphabets}")
    print(f"Capital Alphabets: {capital_alphabets}")
    print(f"Spaces: {spaces}")
    print(f"Digits: {digits}")
    print(f"Special Characters: {special_characters}")


input_str = input("Enter a string: ")
displayCounts(input_str)
