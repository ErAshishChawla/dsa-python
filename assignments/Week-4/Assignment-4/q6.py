def joinString(s: str, chr: str) -> str:
    return chr.join(s.split())


print(joinString("python is great", "-"))
