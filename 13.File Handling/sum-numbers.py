def sumNumbers(file_name: str) -> int:
    try:
        f = open(file_name, "r")
        data = f.readlines()
        f.close()

        sum = 0
        for num in data:
            sum += int(num)
        return sum
    except FileNotFoundError:
        print("File not found")
        return -1
    except:
        print("Something went wrong")
        return -1


print(sumNumbers("digits.txt"))
