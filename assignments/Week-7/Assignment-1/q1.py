class Employee:
    def __init__(self, name="Anonymous", age=0, gender="Not Specified", phone_number=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

    def monthlySalary(self, hourly_rate=0, hours_worked=0):
        return hourly_rate * hours_worked

    def yearly_salary(self, hourly_rate=0, hours_worked=0):
        return self.monthlySalary(hourly_rate, hours_worked) * 12


e1 = Employee("John", 25, "Male", 1234567890)
print(e1.monthlySalary(100, 40))
print(e1.yearly_salary(100, 40))
