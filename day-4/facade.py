# facade pattern in python


class Product:
    def __init__(self, id):
        self.id = id


class Inventory:
    def check_inventory(self, product):
        print(f"Checked inventory for product {product.id}")
        return True


class Payment:
    def make_payment(self):
        print("Made payment")
        return True


class Shipping:
    def ship_product(self, product):
        print(f"Shipped product {product.id}")


class OrderFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()

    def place_order(self, product_id):
        product = Product(product_id)
        if self.inventory.check_inventory(product):
            if self.payment.make_payment():
                self.shipping.ship_product(product)
                print("Order placed successfully")
            else:
                print("Payment failed")
        else:
            print("Product out of stock")


# Client code
order_facade = OrderFacade()
order_facade.place_order(
    "P1234"
)  # Prints: Checked inventory for product P1234, Made payment, Shipped product P1234, Order placed successfully
