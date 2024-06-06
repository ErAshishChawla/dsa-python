def countConsonants(s):
    count = 0
    for i in s:
        if i not in "aeiouAEIOU" and ("a" <= i <= "z" or "A" <= i <= "Z"):
            count += 1
    return count


def countVowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count += 1
    return count


def countConstantsAndVowels(s):
    return countConsonants(s), countVowels(s)


s = input("Enter a string: ")
print(countConstantsAndVowels(s))
