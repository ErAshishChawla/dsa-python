def customReplace(s, old, new):
    if old == new:
        return s

    return "".join([char if char != old else new for char in s])


print(customReplace("python is a great language", " ", "-"))
