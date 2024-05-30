class Observer:
    def update(self, message):
        raise NotImplementedError


class UserNotification(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name}, {message}")


class SellerNotification(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name}, {message}")


class Inventory:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify_all(self):
        for observer in self.observers:
            observer.update(f"The product {self.product_name} is out of stock.")

    def sell(self):
        self.quantity -= 1
        if self.quantity == 0:
            self.notify_all()

    def add_stock(self, quantity):
        self.quantity += quantity


# Client code
iphone = Inventory("iPhone 15", 1)

# Create users and seller
alice = UserNotification("Alice")
bob = UserNotification("Bob")
seller = SellerNotification("Seller")

# Register users and seller
iphone.register(alice)
iphone.register(bob)
iphone.register(seller)

# Sell product until it's out of stock
iphone.sell()
iphone.add_stock(2)
