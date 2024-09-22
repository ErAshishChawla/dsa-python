def extractVowels(s: str) -> str:
    vowels = "aeiouAEIOU"

    return "".join([char for char in s if char in vowels])


print(extractVowels("Hello World"))
print(extractVowels("Python Programming"))
