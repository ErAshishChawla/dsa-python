def readLastNLines(src: str, n: int) -> list | None:
    try:
        f = open(src, "r")
        data = f.readlines()
        f.close()

        formatted_data = [line.strip() for line in data]

        if n > len(formatted_data):
            print("Not Enough Lines")
            return
        else:
            return formatted_data[-1 : -n - 1 : -1]
    except FileNotFoundError:
        print("File not found")
        return
    except Exception as e:
        print("Something went wrong")
        print(e)
        return


print(readLastNLines("numbers.txt", 3))
