class Bookstore:
    inventory = {}
    sales_data = []

    def add_book(
        self, isbn: str, name: str, author: str, price: float, quantity: int
    ) -> None:
        if isbn in self.inventory.keys():
            print("Book already exists")
            return

        self.inventory[isbn] = {
            "name": name,
            "author": author,
            "price": price,
            "quantity": quantity,
        }

    def search_book(self, search_criteria: int) -> None:
        if search_criteria == 1:
            isbn = input("Enter the ISBN to search: ")
            if isbn in self.inventory.keys():
                print(f"Name: {self.inventory[isbn]['name']}")
                print(f"Author: {self.inventory[isbn]['author']}")
                print(f"Price: {self.inventory[isbn]['price']}")
                print(f"Quantity: {self.inventory[isbn]['quantity']}")

        elif search_criteria == 2:
            name = input("Enter the name to search: ").lower()
            for isbn, book in self.inventory.items():
                if book["name"].lower() == name:
                    print(f"ISBN: {isbn}")
                    print(f"Author: {book['author']}")
                    print(f"Price: {book['price']}")
                    print(f"Quantity: {book['quantity']}")

        elif search_criteria == 3:
            author = input("Enter the author to search: ").lower()
            for isbn, book in self.inventory.items():
                if book["author"].lower() == author:
                    print(f"ISBN: {isbn}")
                    print(f"Name: {book['name']}")
                    print(f"Price: {book['price']}")
                    print(f"Quantity: {book['quantity']}")

        else:
            print("Invalid choice")

    def update_quantity(self, isbn: str, new_quantity: int) -> None:
        if isbn not in self.inventory.keys():
            print("Book not found")
            return

        self.inventory[isbn]["quantity"] = new_quantity

    def process_order(self, isbn: str, quantity: int, customer_name: str) -> None:
        if isbn not in self.inventory.keys():
            print("Book not found")
            return

        if self.inventory[isbn]["quantity"] < quantity:
            print("Insufficient quantity")
            return

        self.inventory[isbn]["quantity"] -= quantity
        self.sales_data.append(
            {
                "isbn": isbn,
                "quantity": quantity,
                "customer_name": customer_name,
                "price_per_item": self.inventory[isbn]["price"],
                "total_price": quantity * self.inventory[isbn]["price"],
            }
        )

    def get_sales_report(self) -> None:
        print("Sales Report:")
        total_revenue = sum([sale["total_price"] for sale in self.sales_data])
        total_books_sold = sum([sale["quantity"] for sale in self.sales_data])
        print(f"Total Revenue: {total_revenue}")
        print(f"Total Books Sold: {total_books_sold}")

    def display_inventory(self) -> None:
        print("Inventory:")
        for isbn, book in self.inventory.items():
            print(f"ISBN: {isbn}")
            print(f"Name: {book['name']}")
            print(f"Author: {book['author']}")
            print(f"Price: {book['price']}")
            print(f"Quantity: {book['quantity']}")
            print()

    def display_sales_data(self) -> None:
        print("Sales Data:")
        for sale in self.sales_data:
            print(f"ISBN: {sale['isbn']}")
            print(f"Customer Name: {sale['customer_name']}")
            print(f"Quantity: {sale['quantity']}")
            print(f"Price per item: {sale['price_per_item']}")
            print(f"Total Price: {sale['total_price']}")
            print()


book_store = Bookstore()


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Update Quantity")
    print("4. Process Order")
    print("5. Get Sales Report")
    print("6. Display Inventory")
    print("7. Display Sales Data")
    print("8. Exit\n")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input")
        continue
    except:
        print("An error occurred")
        continue

    if choice == 1:
        isbn = input("Enter the ISBN of the book: ")
        name = input("Enter the name of the book: ")
        author = input("Enter the author of the book: ")
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

        book_store.add_book(isbn, name, author, price, quantity)

    elif choice == 2:
        print("\nSearch Criteria:")
        print("1. ISBN")
        print("2. Name")
        print("3. Author")
        print("4. Exit Search\n")

        try:
            search_criteria = int(input("Enter your choice: "))

        except ValueError:
            print("Invalid input")
            continue
        except:
            print("An error occurred")
            continue

        if search_criteria == 4:
            continue

        book_store.search_book(search_criteria)

    elif choice == 3:
        isbn = input("Enter the ISBN of the book: ")
        try:
            new_quantity = int(input("Enter the new quantity: "))
        except ValueError:
            print("Invalid input")
            continue

        book_store.update_quantity(isbn, new_quantity)

    elif choice == 4:
        isbn = input("Enter the ISBN of the book: ")
        try:
            quantity = int(input("Enter the quantity: "))
        except ValueError:
            print("Invalid input")
            continue
        customer_name = input("Enter the customer name: ")

        book_store.process_order(isbn, quantity, customer_name)

    elif choice == 5:
        book_store.get_sales_report()

    elif choice == 6:
        book_store.display_inventory()

    elif choice == 7:
        book_store.display_sales_data()

    elif choice == 8:
        break
