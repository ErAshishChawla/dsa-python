import random


class Bank:
    def __init__(self):
        self.account_holder_name = input("Enter the account holder name: ").title()
        self.account_number = random.randint(100000, 999999)
        self.balance = 100.0
        self.account_type = input("Enter the account type: ").title()

    def displayAllInfo(self):
        print(f"\nAccount Holder Name: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: {self.balance}")
        print(f"Account Type: {self.account_type}\n")

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid Amount")
            return
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Updated Balance: {self.balance}")

    def deposit(self, amount):
        if amount < 0:
            print("Invalid Amount")
            return
        else:
            self.balance += amount
            print(f"Updated Balance: {self.balance}")

    def getBalance(self):
        return self.balance


account1 = Bank()

account1.displayAllInfo()

account1.deposit(1000.00)

account1.withdraw(2000.00)

current_balance = account1.getBalance()
print(f"Current Balance: {current_balance}")
