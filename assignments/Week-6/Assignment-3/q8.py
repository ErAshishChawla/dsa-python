def JToI(file_name: str) -> int | str:
    try:
        f = open(file_name, "r")
        characters = f.read()
        for i in range(len(characters)):
            if characters[i] == "J":
                characters = characters[:i] + "I" + characters[i + 1 :]
            elif characters[i] == "j":
                characters = characters[:i] + "i" + characters[i + 1 :]
        return characters
    except Exception as e:
        print(e)
        return -1


print(JToI("test.txt"))
