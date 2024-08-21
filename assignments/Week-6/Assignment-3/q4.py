def getCountOfThe(file_name: str) -> int:
    try:
        count = 0
        f = open(file_name, "r")
        list_of_words = f.read().split()
        f.close()
        for line in list_of_words:
            if line.lower() == "the":
                count += 1

        return count
    except Exception as e:
        print(e)
        return -1


print(getCountOfThe("test.txt"))
