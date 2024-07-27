actual = ""
result = ""


def flipCase(s: str) -> str:
    temp_string = ""
    upper_a = ord("A")
    upper_z = ord("Z")
    lower_a = ord("a")
    lower_z = ord("z")

    for i in s:
        if upper_a <= ord(i) <= upper_z:
            # Convert to lower
            temp_string += chr(ord(i) + lower_a - upper_a)
        elif lower_a <= ord(i) <= lower_z:
            # convert it to upper
            temp_string += chr(ord(i) - (lower_a - upper_a))
        else:
            temp_string += i
    return temp_string


while True:
    s = input("Enter a string:")
    if s.lower() == "q":
        break
    actual += s
    actual += "\n"
    result += flipCase(s)
    result += "\n"

print(result)
