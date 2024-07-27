def joinReverse(s: str, chr: str) -> str:
    return chr.join(s.split()[::-1])


print(joinReverse("python is great", "-"))
