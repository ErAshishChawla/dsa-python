def isLetterAndNumberPresent(s: str) -> bool:
    isLetterPresent = False
    isNumberPresent = False

    for i in s:
        if "a" <= i <= "z" or "A" <= i <= "Z":
            isLetterPresent = True
        elif "0" <= i <= "9":
            isNumberPresent = True

    return isLetterPresent and isNumberPresent


print(isLetterAndNumberPresent("Hello World!"))
print(isLetterAndNumberPresent("Hello World 123!"))
