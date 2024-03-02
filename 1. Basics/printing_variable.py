"""
Ways to print a variable in python
"""

name = "Ashish"
age = 16
gender = "Male"

print(name, age, gender)

# Method 1: Using comma
print("My name is", name)
print("My age is", age)
print("My gender is", gender)
print("My name is ", name, "and my age is", age, "and my gender is", gender)

# Method - 2: (F-strings)
print(f"My name is {name}")
print(f"My age is {age}")
print(f"My gender is {gender}")
print(f"My name is {name} and my age is {age} and my gender is {gender}")

print(f"name = {name}")
print(f"{name, age =}")
