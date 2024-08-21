def getWordCount(file_name: str) -> int:
    try:
        f = open(file_name, "r")
        list_of_words = f.read().split()
        f.close()
        return len(list_of_words)
    except Exception as e:
        print(e)
        return -1


print(getWordCount("test.txt"))
