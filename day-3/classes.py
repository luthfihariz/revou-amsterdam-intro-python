class Car:
    def __init__(self, year, brand="Toyota"):
        self.year = year
        self.brand = brand

    def honk(self):
        if self.year < 2010:
            return "Teeeeet!"
        else:
            return "Tooooot!"
    
    def display_info(self):
        return f"This is a car that made in {self.year} with brand {self.brand}"
    
    def print_info(self):
        print()

car_1 = Car(2018, "Hyundai") # object car_1
print(car_1.display_info())
print(car_1.honk())

car_2 = Car(2005, "Suzuki")
print(car_2.display_info())
print(car_2.honk())

print(car_2.__class__.__name__)