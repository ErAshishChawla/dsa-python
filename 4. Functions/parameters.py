"""
Parameters
"""


def console(x: int, y: int, z: int):
    print(f"{x =}")
    print(f"{y =}")
    print(f"{z =}")


console(10, 20, 30)

print("-----------------")


def greet(name: str, age: int, gender: str):
    print(f"{name = }")
    print(f"{age = }")
    print(f"{gender = }")


greet("Ashish", 23, "Male")

print("-----------------")


def greet2(name: str, age: int, gender: str):
    name = ""
    age = 0
    gender = ""
    print(f"{name = }")
    print(f"{age = }")
    print(f"{gender = }")


name = "Ashish"
age = 23
gender = "Male"
greet2(name, age, gender)
print(name, age, gender)

print("-----------------")
