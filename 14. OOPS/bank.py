import random
from typing import List


class Bank:
    def __init__(self) -> None:
        self.account_number = random.randint(1000000, 999999999)
        self.holder = input("Enter the account holder name: ").title()
        self.balance = 0.0
        self.account_type = input("Enter the account type: ").title()

    def display(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Holder: {self.holder}")
        print(f"Account Balance: {self.balance}")
        print(f"Account Type: {self.account_type}\n")

    def withdraw(self):
        amt = float(input("Enter the amount to withdraw: "))
        if amt < 0:
            print("Invalid Amount")
            return
        elif amt > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amt
            print(f"Updated Balance: {self.balance}")

    def deposit(self):
        amt = float(input("Enter the amount to deposit: "))
        if amt < 0:
            print("Invalid Amount")
            return
        else:
            self.balance = self.balance + amt
            print(f"Updated Balance: {self.balance}")

    def getBalance(self):
        print(f"Account Balance: {self.balance}")


accounts: List[Bank] = []

while True:
    print("\n1. Create account")
    print("2. Display all accounts")
    print("3. Search account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Transfer")
    print("7. Exit\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = Bank()
        accounts.append(x)
    elif choice == 2:
        for obj in accounts:
            obj.display()
    elif choice == 3:
        search_acc = int(input("Enter the account number to search: "))

        for obj in accounts:
            if obj.account_number == search_acc:
                obj.display()
                break
        else:
            print("Account not found")
    elif choice == 4:
        search_acc = int(input("Enter the account number to deposit: "))

        for obj in accounts:
            if obj.account_number == search_acc:
                obj.deposit()
                break
        else:
            print("Account not found")
    elif choice == 5:
        search_acc = int(input("Enter the account number to withdraw: "))

        for obj in accounts:
            if obj.account_number == search_acc:
                obj.withdraw()
                break
        else:
            print("Account not found")
    elif choice == 6:
        search_parent_acc = int(input("Enter the account number to transfer from: "))
        search_child_acc = int(input("Enter the account number to transfer to: "))
        amount = float(input("Enter the amount to transfer: "))

        matching_parent = None
        matching_child = None

        for obj in accounts:
            if obj.account_number == search_parent_acc:
                matching_parent = obj
            elif obj.account_number == search_child_acc:
                matching_child = obj

        # Now we have both the parent and child account objects
        if matching_parent is None or matching_child is None:
            print("Account not found")
        else:
            if amount < 0:
                print("Invalid Amount")
            elif amount > matching_parent.balance:
                print("Insufficient Balance")
            else:
                matching_parent.balance -= amount
                matching_child.balance += amount
                print("Transfer Successful")
                print(f"Updated Balance of Parent: {matching_parent.balance}")
                print(f"Updated Balance of Child: {matching_child.balance}")
    elif choice == 7:
        break
    else:
        print("Invalid Choice")
