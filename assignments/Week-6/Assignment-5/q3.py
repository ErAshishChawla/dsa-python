def wordsToNumber(s):
    wordToNumMap = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    return "".join([wordToNumMap[n] for n in s.split() if n in wordToNumMap])


print(wordsToNumber("zero four zero one"))
print(wordsToNumber("four zero one four"))
