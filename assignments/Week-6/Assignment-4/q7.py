def reverseLines(src: str, dest: str) -> int | None:
    try:
        f = open(src, "r")
        data = f.readlines()
        f.close()

    except FileNotFoundError:
        print("File not found")
        return -1
    except:
        print("Something went wrong")
        return -1

    formatted_data = [line.strip() for line in data]

    try:
        f = open(dest, "w")
        for line in formatted_data[::-1]:
            f.write(f"{line}\n")
        f.close()
    except:
        print("Something went wrong")
        return -1


reverseLines("test-q7.txt", "result-q7.txt")
