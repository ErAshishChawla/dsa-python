def sumDigits(file_name: str) -> int:
    try:
        f = open(file_name, "r")
        data = f.read()
        f.close()

        digits = "0123456789"
        sum = 0
        for char in data:
            if char in digits:
                sum += int(char)

        return sum
    except FileNotFoundError:
        print("File not found")
        return -1
    except:
        print("Something went wrong")
        return -1


print(sumDigits("test.txt"))
