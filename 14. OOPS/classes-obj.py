from typing import Any


class Student:

    def __init__(self, roll_no: int, name: str, age: int, gender: str) -> None:
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return f"\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nRoll No: {self.roll_no}\n"

    def __add__(self, other):
        return self.age + other.age

    def __len__(self):
        return self.age

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __le__(self, other):
        return self.age <= other.age

    def updateName(self):
        self.name = input("Enter new name: ")

    def updateAge(self, new_age: int):
        self.age = new_age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Roll No: ", self.roll_no)


s1 = Student(1, "Ashish", 25, "Male")
s2 = Student(2, "Komal", 25, "Female")
s3 = Student(3, "Rahul", 27, "Male")

print(s1 >= s2)
