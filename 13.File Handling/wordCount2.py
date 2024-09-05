def wordCount(fileName: str) -> int:
    try:
        f = open(fileName, "r")
        data = f.read()
        f.close()

        words = data.split()
        return len(words)
    except FileNotFoundError:
        print("File not found")
        return -1
    except:
        print("Something went wrong")
        return -1


print(wordCount("test.txt"))
