def printFirstAndLastTwo(s: str) -> str:
    if len(s) < 3:
        print("Invalid")
        return

    return s[:2] + s[-2:]


print(printFirstAndLastTwo("aeroplane"))
