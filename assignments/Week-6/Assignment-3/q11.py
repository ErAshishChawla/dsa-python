def printWordsInReverse(file_name: str) -> int | str:
    try:
        f = open(file_name, "r")
        lines = f.readlines()
        f.close()
        reversed_word_lines = ""
        for line in lines:
            words = line.strip().split()
            reversed_words = [word[::-1] for word in words]
            reversed_word_lines = reversed_word_lines + " ".join(reversed_words) + "\n"

        return reversed_word_lines
    except Exception as e:
        print(e)
        return -1


print(printWordsInReverse("test3.txt"))
