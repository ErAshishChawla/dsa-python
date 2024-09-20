class Product:
    def __init__(
        self, name="Not specified", price=0, category="Not specified", quantity=0
    ):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    def total_cost(self, discount_percent=0):
        original_cost = self.price * self.quantity
        discount = original_cost * discount_percent / 100
        return original_cost - discount


p1 = Product("Laptop", 50000, "Electronics", 10)
print(p1.total_cost(10))
p2 = Product("Mobile", 20000, "Electronics", 5)
print(p2.total_cost(5))
