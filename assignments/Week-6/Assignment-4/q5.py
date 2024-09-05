def generateFiles():
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for i in alphabets:
        try:
            f = open(f"{i.upper()}.txt", "w")
            f.close()
        except:
            print("Something went wrong")
            return


generateFiles()
