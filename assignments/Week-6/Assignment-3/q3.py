def getCountOfLinesNotStartingWithTort(file_name: str) -> int:
    try:
        count = 0
        f = open(file_name, "r")
        list_of_lines = f.readlines()
        for line in list_of_lines:
            santized_line = line.strip()
            if not santized_line[0] == "t" and not santized_line[0] == "T":
                count += 1
        f.close()
        return count
    except Exception as e:
        print(e)
        return -1


print(getCountOfLinesNotStartingWithTort("test.txt"))
