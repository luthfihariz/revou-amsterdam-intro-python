class Dog:
    def sound(self):
        return "Woof!"


class Cat:
    def sound(self):
        return "Meow!"


class Car:
    def sound(self):
        return "Broom!"


class Person:
    def speak(self):
        return "Hey!"

def make_sound(athing):
    print(athing.sound())


def display_price(product):
    print(f"Rp {product.get_price()}")


dog = Dog()
cat = Cat()
car = Car()
person = Person()

make_sound(dog)
make_sound(cat)
make_sound(car)
#make_sound(person)