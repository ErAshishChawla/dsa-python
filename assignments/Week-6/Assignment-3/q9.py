def calculateTotal(file_name: str):
    try:
        f = open(file_name, "r")
        numbers = list(map(int, f.readlines()))
        f.close()
        total = 0
        for number in numbers:
            total += number

        return total
    except Exception as e:
        print(e)
        return -1


print(calculateTotal("test2.txt"))
