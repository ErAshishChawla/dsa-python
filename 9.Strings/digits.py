# a = input("Enter a")
# b = input("Enter b")

# if a.isdigit() and b.isdigit():
#     print(float(a) + float(b))
# else:
#     print(a + b)

# Ascii method


def checkDigit(s: str):
    ascii_0 = ord("0")
    ascii_9 = ord("9")
    for i in s:
        if ord(i) < ascii_0 or ord(i) > ascii_9:
            return False
    return True


a = "123"
b = "456"

if checkDigit(a) and checkDigit(b):
    print(float(a) + float(b))
else:
    print(a + b)

print("abcefdewfb".find("p"))
