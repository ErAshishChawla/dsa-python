def getCountOfWordsThatEndWithE(file_name: str) -> int:
    try:
        count = 0
        f = open(file_name, "r")
        list_of_words = f.read().strip().split()
        f.close()
        for word in list_of_words:
            if word[-1].lower() == "e":
                count = count + 1

        return count
    except Exception as e:
        print(e)
        return -1


print(getCountOfWordsThatEndWithE("test.txt"))
