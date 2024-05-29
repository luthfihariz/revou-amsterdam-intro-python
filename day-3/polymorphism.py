class Dog:
    def sound(self):
        return "Woof!"


class Cat:
    def sound(self):
        return "Meow!"


def make_sound(animal):
    print(animal.sound())


dog = Dog()
cat = Cat()

make_sound(dog)  # Prints: Woof!
make_sound(cat)  # Prints: Meow!
