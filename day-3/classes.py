class Car:
    def __init__(self, make, model, year): # Constructor
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def honk(self):
        return "Tet tot!"


my_car = Car("Toyota", "Corolla", 2019)
print(my_car.display_info())
print(my_car.honk())
