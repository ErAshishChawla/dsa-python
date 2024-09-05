def writeMultiplication(dest: str, num: int) -> None:
    try:
        f = open(dest, "w")
        for i in range(1, 11):
            f.write(f"{num} x {i} = {num*i}\n")
        f.close()
    except:
        print("Something went wrong")
        return

    return


writeMultiplication("multiplication.txt", 5)
