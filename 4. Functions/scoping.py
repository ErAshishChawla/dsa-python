def add():
    num1: int = int(input("Enter num1= "))
    num2: int = int(input("Enter num2= "))
    print(num1 + num2)


num1: int = 100
num2: int = 200

add()

print(
    num1, num2
)  # these will be from global scope. Once function is executed, it will not affect the global scope variables.
