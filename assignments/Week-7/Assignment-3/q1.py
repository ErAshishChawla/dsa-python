from typing import List
import random


class Book:
    def __init__(self, name: str, price: float, quantity: int):
        self.isbn = str(random.randint(100000, 999999))
        self.name = name
        self.price = price
        self.quantity = quantity
        self.rented_books = 0

    def __str__(self):
        return f"\nISBN: {self.isbn}\nName: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nRented Books: {self.rented_books}\n"

    def __len__(self):
        return self.quantity

    def rent(self):
        if self.rented_books >= self.quantity:
            print("No books available")
            return
        self.rented_books += 1
        print("Book rented successfully")


library: List[Book] = []

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Check Quantity")
    print("4. Rent Book")
    print("5. Display Books")
    print("6. Exit\n")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name of the book: ")
            try:
                price = float(input("Enter the price of the book: "))
            except ValueError:
                print("Invalid input")
                continue
            try:
                quantity = int(input("Enter the quantity of the book: "))
            except ValueError:
                print("Invalid input")
                continue
            is_rented = False

            b = Book(name, price, quantity)
            library.append(b)

        elif choice == 2:
            search_isbn = input("Enter the ISBN to search: ")

            for book in library:
                if book.isbn == search_isbn:
                    print(book)
                    break

        elif choice == 3:
            search_isbn = input("Enter the ISBN to check quantity: ")

            for book in library:
                if book.isbn == search_isbn:
                    print(f"Quantity: {len(book)}")
                    break

        elif choice == 4:
            search_isbn = input("Enter the ISBN to rent: ")

            for book in library:
                if book.isbn == search_isbn:
                    book.rent()
                    break

        elif choice == 5:
            for book in library:
                print(book)

        elif choice == 6:
            break

    except ValueError:
        print("Invalid choice")
        continue
    except:
        print("An error occurred")
        continue
