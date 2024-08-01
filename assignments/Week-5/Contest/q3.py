def converUppercase(s: str):
    upper_count = 0

    for i in s[:4]:
        if i.isupper():
            upper_count += 1

    if upper_count >= 2:
        return s.upper()

    return s


print(converUppercase("pyTHon"))
print(converUppercase("helLo"))
print(converUppercase("gOOD"))
