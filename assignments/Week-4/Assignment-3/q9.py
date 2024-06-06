def printSecondHalf(s: str) -> str:
    half_index = len(s) // 2 + 1
    return s[half_index:]


print(printSecondHalf("aeroplane"))  # plane
print(printSecondHalf("delhi"))  # hon
print(printSecondHalf("pavbhaji"))  # hon
