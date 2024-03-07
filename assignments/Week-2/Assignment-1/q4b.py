def getSalary(salary: float):
    if salary < 0:
        print("Invalid input")
    elif salary < 10000:
        salary += salary * 0.05
        print(f"Your salary is {salary:.2f}")
    elif salary >= 10000 and salary <= 20000:
        salary += salary * 0.1
        print(f"Your salary is {salary:.2f}")
    elif salary > 20000 and salary <= 50000:
        salary += salary * 0.15
        print(f"Your salary is {salary:.2f}")
    elif salary > 50000:
        salary += salary * 0.2
        print(f"Your salary is {salary:.2f}")
    else:
        print("Something went wrong.")


salary: float = float(input("Enter your salary: "))
getSalary(salary)
