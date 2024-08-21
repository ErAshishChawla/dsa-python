def printLineInReverse(file_name: str) -> int | str:
    try:
        f = open(file_name, "r")
        lines = f.readlines()
        f.close()
        reversed_lines = ""
        for line in lines:
            words = line.split()
            reversed_lines = reversed_lines + " ".join(words[::-1]) + "\n"

        return reversed_lines
    except Exception as e:
        print(e)
        return -1


print(printLineInReverse("test3.txt"))
