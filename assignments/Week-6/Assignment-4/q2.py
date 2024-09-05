def checkEvenOrOdd(src: str, dest: str) -> None:
    try:
        f = open(src, "r")
        data = f.read().split()
        f.close()
    except FileNotFoundError:
        print("File not found")
        return
    except Exception as e:
        print("Something went wrong")
        print(e)
        return

    try:
        f = open(dest, "w")
        for num in data:
            if int(num) % 2 == 0:
                f.write(f"{num} even\n")
            else:
                f.write(f"{num} odd\n")
        f.close()
    except:
        print("Something went wrong")
        return

    return


checkEvenOrOdd("numbers.txt", "numbers_result.txt")
