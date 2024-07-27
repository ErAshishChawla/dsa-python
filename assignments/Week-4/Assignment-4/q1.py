def result(s: str) -> str:
    l = len(s)

    if l == 0:
        return ""
    elif l % 2 != 0:
        return "".join([i.lower() if i.isupper() else i.upper() for i in s])
    else:
        return s[::-1]


a = "AEroPLane"
print(result(a))

a = "AEroPLanes"
print(result(a))
