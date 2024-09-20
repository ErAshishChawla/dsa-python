class Employee:
    def __init__(self, name, age, gender, phone, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.salary = salary

    def change_salary(self, new_salary):
        self.salary = new_salary

    def display_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Phone: ", self.phone)
        print("Salary: ", self.salary)


e1 = Employee("John", 25, "Male", 1234567890, 1000)
e1.display_details()

e1.change_salary(2000)
e1.display_details()
