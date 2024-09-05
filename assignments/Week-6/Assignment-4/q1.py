def copyFileContent(source, destination):
    try:
        f = open(source, "r")
        data = f.read()
        f.close()
    except FileNotFoundError:
        print("File not found")
        return -1
    except Exception as e:
        print("Something went wrong")
        print(e)
        return -1

    try:
        f = open(destination, "w")
        f.write(data)
        f.close()
        return 1
    except:
        print("Something went wrong")
        return -1


copyFileContent("test-q1.txt", "result-q1.txt")
