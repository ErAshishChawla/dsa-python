def snakeToPascal(s):
    s = s.split("_")
    return "".join([i.capitalize() for i in s])


print(snakeToPascal("hello_world"))  # HelloWorld
print(snakeToPascal("snake_to_pascal"))  # SnakeToPascal
