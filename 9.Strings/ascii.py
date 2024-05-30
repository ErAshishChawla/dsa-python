a = "PythOn is A GreAT LangAUGE"

count = 0
for char in a:
    ascii_number = ord(char)

    if ascii_number >= 65 and ascii_number <= 90:
        count += 1
print("Total uppercase letters:", count)

count = 0
for char in a:
    if "A" <= char <= "Z":
        count += 1
print("Total uppercase letters:", count)


a = "Pyth1On is A Gre3AT La1ngAU3 GE"

count = 0
minAscii = ord("0")
maxAscii = ord("9")
for char in a:
    ascii_number = ord(char)

    if ascii_number >= minAscii and ascii_number <= maxAscii:
        count += 1
print("Total digits", count)

count = 0
for char in a:
    ascii_number = ord(char)

    if "0" <= char <= "9":
        count += 1
print("Total digits", count)
