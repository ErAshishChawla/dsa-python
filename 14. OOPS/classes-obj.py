class Student:

    def __init__(self):
        self.roll_no = int(input("Enter Roll No: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")

    def updateName(self):
        self.name = input("Enter new name: ")

    def updateAge(self, new_age: int):
        self.age = new_age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Roll No: ", self.roll_no)


s1 = Student()

s1.display()
