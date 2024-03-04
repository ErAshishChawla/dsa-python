"""
Statically typed languages require you to declare the type of a variable before you use it.
Python is a dynamically typed language, so you don't have to declare the type of a variable when you create one.

Annotations define the type of a variable, but they don't enforce it. They are just hints to the developer and tools like linters and type checkers.
"""

a: int | str = 5
print(a)

a = 432
print(a)

a = "hello"

b: int | float = 5
print(b)
