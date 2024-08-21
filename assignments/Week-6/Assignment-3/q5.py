def getCountOfThe(file_name: str) -> int | None:
    try:
        f = open(file_name, "r")
        list_of_words = f.read().split()
        for word in list_of_words:
            if len(word) > 4:
                print(word)
        f.close()
    except Exception as e:
        print(e)
        return -1


getCountOfThe("test.txt")
