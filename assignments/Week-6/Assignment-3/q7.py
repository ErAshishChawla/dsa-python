def getUpperCaseCharactersInFile(file_name: str) -> int:
    try:
        count = 0
        f = open(file_name, "r")
        characters = f.read().strip()
        f.close()
        for char in characters:
            if char.isupper():
                count += 1
        return count
    except Exception as e:
        print(e)
        return -1


print(getUpperCaseCharactersInFile("test.txt"))
