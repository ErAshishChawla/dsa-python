"""
Default parameters

All parameters in a function are required until, you set a default value for them.
"""


def totalMarks(
    physics: int,
    chemistry: int = 0,
    maths: int = 55,
    english: int = 0,
    computer: int = 0,
):
    total = physics + chemistry + maths + english + computer
    print(f"Total Marks= {total}")


totalMarks(98)

print("-----------------")


def greet(name: str, age: int, gender: str = "Not Specified"):
    print(f"{name=}")
    print(f"{age=}")
    print(f"{gender=}")


greet("Ashish", gender="Male", age=23)
