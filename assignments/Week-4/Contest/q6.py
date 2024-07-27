def checkLowercase(s: str) -> bool:
    lower_a = ord("a")
    lower_z = ord("z")

    if lower_a <= ord(s) <= lower_z:
        return True
    return False


def checkUppercase(s: str) -> bool:
    upper_a = ord("A")
    upper_z = ord("Z")

    if upper_a <= ord(s) <= upper_z:
        return True
    return False


def checkDigit(s: str) -> bool:
    digit_0 = ord("0")
    digit_9 = ord("9")

    if digit_0 <= ord(s) <= digit_9:
        return True
    return False


def checkSpecial(s: str) -> bool:
    if not checkLowercase(s) and not checkUppercase(s) and not checkDigit(s):
        return True
    return False


def passwordStrength(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(checkLowercase(i) for i in password):
        return False
    if not any(checkUppercase(i) for i in password):
        return False
    if not any(checkDigit(i) for i in password):
        return False
    if not any(checkSpecial(i) for i in password):
        return False
    return True


print(passwordStrength("Python1$"))
print(passwordStrength("anirudh"))
