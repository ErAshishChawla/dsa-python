def getLinesCount(file_name: str) -> int:
    try:
        f = open(file_name, "r")
        list_of_lines = f.readlines()
        f.close()
        return len(list_of_lines)
    except Exception as e:
        print(e)
        return -1


print(getLinesCount("test.txt"))
